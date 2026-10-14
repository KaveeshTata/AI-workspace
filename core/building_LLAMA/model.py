import math
import inspect
from dataclasses import dataclass
import torch
import torch.nn as nn
import torch.nn.functional as F

# Did not use LayerNorm Module from torch.nn because it does not have an option to disable bias. The bias is not used in the original GPT2 model, so we need to implement our own LayerNorm module.
class RMSNorm(nn.Module):
    def __init__(self, ndim):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(ndim))

    # Using the rms_norm function from torch.nn.functional
    def forward(self, input):
        return F.rms_norm(input, self.weight.shape, self.weight, 1e-5)


# Causal self-attention layer with flash attention support, Flash requires PyTorch 2.0 or higher and a GPU with CUDA 11.8 or higher. If flash attention is not available, it will fall back to the standard implementation.
class CausalAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.head_size = config.n_embd // config.n_head
        assert self.head_size * self.n_head == self.n_embd, "Embedding dimension must be divisible by number of heads"

        #Initialize the linear layers for query, key, value and output projection. The input dimension is n_embd and the output dimension is 3 * n_embd for q, k, v and n_embd for the output projection.
        self.c_attn = nn.Linear(config.n_embd, 3 * config.n_embd, bias=config.bias)
        self.c_proj = nn.Linear(config.n_embd, config.n_embd, bias=config.bias)
        #Dropout layers for attention and residual connections. The dropout probability is specified in the config.
        self.attn_dropout = nn.Dropout(config.attn_pdrop)
        self.resid_dropout = nn.Dropout(config.resid_pdrop)
        self.n_head = config.n_head
        self.n_embd = config.n_embd
        self.dropout = config.dropout

        self.flash = hasattr(torch.nn.functional, 'scaled_dot_product_attention') and config.use_flash_attention
        if not self.flash:
            self.register_buffer("bias", torch.tril(torch.ones(config.block_size, config.block_size)).view(1, 1, config.block_size, config.block_size))

    #RoPE for LLAMA model from the original paper "LLaMA: Open and Efficient Foundation Language Models" by Hugo Touvron et al.
    def apply_rotary_position_embeddings(self, q, k, base=10000):
        B, H, D, T = q.shape
        assert D % 2 == 0, "Embedding dimension must be even for rotary embeddings"
        position_ids = torch.arange(T, device=q.device)

        inv_freqs = 1.0 / (base ** torch.arange(0, D, 2, device=q.device) / D)
        angles = torch.outer(position_ids.to(torch.float32), inv_freqs)
        cos = torch.repeat_interleave(angles.cos(), 2, dim=-1)[None, None, :, :]
        sin = torch.repeat_interleave(angles.sin(), 2, dim=-1)[None, None, :, :]

        def rotate_pairs(x):
            x_rot = torch.stack((-x[..., 1::2], x[..., ::2]),dim=-1)
            return x_rot.flatten(-2)

        q_rot = q * cos.to(q.dtype) + rotate_pairs(q) * sin.to(q.dtype)
        k_rot = k * cos.to(k.dtype) + rotate_pairs(k) * sin.to(k.dtype)
        return q_rot, k_rot

    # The main attention forward pass. With flash attention and residual dropout
    def forward(self, x):
        B, T, C = x.size()

        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)  # (B, nh, T, hs)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)  # (B, nh, T, hs)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)  # (B, nh, T, hs)

        q,k = self.apply_rotary_position_embeddings(q, k)

        if self.flash:
            y = F.scaled_dot_product_attention(q, k, v, attn_mask=None, dropout_p=self.dropout if self.training else 0.0, is_causal=True)

        else:
            att = (q @ k.transpose(-2, -1)) * (1.0 / (k.size(-1) ** 0.5))
            att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float('-inf'))
            att = F.softmax(att, dim=-1)
            att = self.attn_dropout(att)
            y = att @ v  # (B, nh, T, hs)

        y = y.transpose(1, 2).contiguous().view(B, T, C)  # re-assemble all head outputs side by side
        y = self.resid_dropout(self.c_proj(y))
        return y



# SWIGLUMLP block, this is the Feed Forward network or FFN at the end of each transformer block for LLAMA models. It uses the SwiGLU activation function, which is a variant of the GELU activation function. The hidden dimension is 8/3 times the embedding dimension, as per the original GPT2 paper.
class SwiGLUMLP(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.silu = nn.SiLU()

        hidden = int(8 * config.n_embd // 3)
        self.w_gate = nn.Linear(config.n_embd, hidden, bias=config.bias)
        self.w_value = nn.Linear(config.n_embd, hidden, bias=config.bias)
        self.w_out = nn.Linear(hidden, config.n_embd, bias=config.bias)
        self.dropout = nn.Dropout(config.resid_pdrop)

    def forward(self, x):
        x = self.w_gate(x) * self.silu(self.w_value(x))
        x = self.w_out(x)
        x = self.dropout(x)
        return x

# Transformer block. The main building block of the GPT2 model. LayerNorm -> CausalAttention -> LayerNorm -> MLP. The residual connections are added after each sub-layer.
class Block(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.ln_1 = RMSNorm(config.n_embd)
        self.attn = CausalAttention(config)
        self.ln_2 = RMSNorm(config.n_embd)
        self.mlp = SwiGLUMLP(config)

    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x

# GPT-2 config as per the original paper
@dataclass
class GPT2Config:
    n_embd: int = 768
    n_head: int = 12
    n_layer: int = 12
    block_size: int = 1024
    vocab_size: int = 50304     #increased vocab size to 50304 from 50257 for faster processing in the GPUs
    bias: bool = True
    dropout: float = 0.1


# The main GPT2 model class. It contains the embedding layers, transformer blocks, and the final linear layer for language modeling.
class GPT2(nn.Module):
    def __init__(self, config):
        super().__init__()
        assert config.vocab_size is not None, "vocab_size must be specified"
        assert config.block_size is not None, "block_size must be specified"
        self.config = config

        # From embedings to transformer blocks to final layer norm. The transformer is a ModuleDict containing the embedding layers, dropout, transformer blocks, and final layer norm.
        self.transformer = nn.ModuleDict(dict(
            wte = nn.Embedding(config.vocab_size, config.n_embd),
            wpe = nn.Embedding(config.block_size, config.n_embd),
            drop = nn.Dropout(config.dropout),
            h = nn.ModuleList([Block(config) for _ in range(config.n_layer)]),
            ln_f = RMSNorm(config.n_embd),            
        ))
        self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)
        # Tie the weights of the lm_head to the token embeddings. This is a common technique in language modeling to reduce the number of parameters and improve generalization. According to the original GPT-2 paper
        self.transformer.wte.weight = self.lm_head.weight  

        self.apply(self._init_weights)
        for pn, p in self.named_parameters():
            if pn.endswith('c_proj.weight'):
                nn.init.normal_(p, mean=0.0, std=0.02/math.sqrt(2 * config.n_layer))

        print("number of parameters: %.2fM" % (self.get_num_params()/1e6,))

    
    # Helper functions
    def get_num_parameters(self, non_embedding=True):
        n_params = sum(p.numel() for p in self.parameters())
        if non_embedding:
            n_params -= self.transformer.wte.weight.numel()
        return n_params

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    # The entire forward pass of the GPT2 model. It takes in a batch of token indices and optionally target indices for computing the loss. It returns the logits and the loss if targets are provided.
    def forward(self, idx, targets=None):
        device = idx.device
        b, t = idx.size()
        assert t <= self.config.block_size, f"Cannot forward sequence of length {t}, block size is only {self.config.block_size}"

        tok_emb = self.transformer.wte(idx)  # token embeddings of shape (b, t, n_embd)
        x = self.transformer.drop(tok_emb)
        for block in self.transformer.h:
            x = block(x)

        x = self.transformer.ln_f(x)
        
        if targets is not None:
            logits = self.lm_head(x)
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1)
        else:
            logits = self.lm_head(x[..., -1, :])
            loss = None

        return logits, loss

    #From https://github.com/karpathy/nanoGPT/blob/master/model.py
    def crop_block_size(self, block_size):
        # model surgery to decrease the block size if necessary
        # e.g. we may load the GPT2 pretrained model checkpoint (block size 1024)
        # but want to use a smaller block size for some smaller, simpler model
        assert block_size <= self.config.block_size
        self.config.block_size = block_size
        self.transformer.wpe.weight = nn.Parameter(self.transformer.wpe.weight[:block_size])
        for block in self.transformer.h:
            if hasattr(block.attn, 'bias'):
                block.attn.bias = block.attn.bias[:,:,:block_size,:block_size]

    #From https://github.com/karpathy/nanoGPT/blob/master/model.py
    @classmethod
    def from_pretrained(cls, model_type, override_args=None):
        assert model_type in {'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'}
        override_args = override_args or {} 
        assert all(k == 'dropout' for k in override_args)
        from transformers import GPT2LMHeadModel
        print("loading weights from pretrained gpt: %s" % model_type)

        config_args = {
            'gpt2':         dict(n_layer=12, n_head=12, n_embd=768),  # 124M params
            'gpt2-medium':  dict(n_layer=24, n_head=16, n_embd=1024), # 350M params
            'gpt2-large':   dict(n_layer=36, n_head=20, n_embd=1280), # 774M params
            'gpt2-xl':      dict(n_layer=48, n_head=25, n_embd=1600), # 1558M params
        }[model_type]
        print("forcing vocab_size=50257, block_size=1024, bias=True")
        config_args['vocab_size'] = 50257 # always 50257 for GPT model checkpoints
        config_args['block_size'] = 1024 # always 1024 for GPT model checkpoints
        config_args['bias'] = True 
        if 'dropout' in override_args:
            print(f"overriding dropout rate to {override_args['dropout']}")
            config_args['dropout'] = override_args['dropout']
        config = GPT2Config(**config_args)
        model = GPT2(config)
        sd = model.state_dict()
        sd_keys = sd.keys()
        sd_keys = [k for k in sd_keys if not k.endswith('.attn.bias')] # discard this mask / buffer, not a param

        # init a huggingface/transformers model
        model_hf = GPT2LMHeadModel.from_pretrained(model_type)
        sd_hf = model_hf.state_dict()

        # copy while ensuring all of the parameters are aligned and match in names and shapes
        sd_keys_hf = sd_hf.keys()
        sd_keys_hf = [k for k in sd_keys_hf if not k.endswith('.attn.masked_bias')] # ignore these, just a buffer
        sd_keys_hf = [k for k in sd_keys_hf if not k.endswith('.attn.bias')] # same, just the mask (buffer)
        transposed = ['attn.c_attn.weight', 'attn.c_proj.weight', 'mlp.c_fc.weight', 'mlp.c_proj.weight']
        # basically the openai checkpoints use a "Conv1D" module, but we only want to use a vanilla Linear
        # this means that we have to transpose these weights when we import them
        assert len(sd_keys_hf) == len(sd_keys), f"mismatched keys: {len(sd_keys_hf)} != {len(sd_keys)}"
        for k in sd_keys_hf:
            if any(k.endswith(w) for w in transposed):
                # special treatment for the Conv1D weights we need to transpose
                assert sd_hf[k].shape[::-1] == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k].t())
            else:
                # vanilla copy over the other parameters
                assert sd_hf[k].shape == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k])

        return model

    def configure_optimizers(self, weight_decay, learning_rate, betas, device_type):
        param_dict = {pn: p for pn, p in self.named_parameters()}
        param_dict = {pn: p for pn, p in param_dict.items() if p.requires_grad}
        decay_params = [p for n, p in param_dict.items() if p.dim() >= 2]
        nodecay_params = [p for n, p in param_dict.items() if p.dim() < 2]
        optim_groups = [
            {'params': decay_params, 'weight_decay': weight_decay},
            {'params': nodecay_params, 'weight_decay': 0.0}
        ]
        num_decay_params = sum(p.numel() for p in decay_params)
        num_nodecay_params = sum(p.numel() for p in nodecay_params)
        print(f"num decayed parameter tensors: {len(decay_params)}, with {num_decay_params:,} parameters")
        print(f"num non-decayed parameter tensors: {len(nodecay_params)}, with {num_nodecay_params:,} parameters")
        fused_available = 'fused' in inspect.signature(torch.optim.AdamW).parameters
        use_fused = fused_available and device_type == 'cuda'
        extra_args = dict(fused=True) if use_fused else dict()
        optimizer = torch.optim.AdamW(optim_groups, lr=learning_rate, betas=betas, **extra_args)
        print(f"using fused AdamW: {use_fused}")

        return optimizer

    #From https://github.com/karpathy/nanoGPT/blob/master/model.py
    def estimate_mfu(self, fwdbwd_per_iter, dt):
        """ estimate model flops utilization (MFU) in units of A100 bfloat16 peak FLOPS """
        # first estimate the number of flops we do per iteration.
        # see PaLM paper Appendix B as ref: https://arxiv.org/abs/2204.02311
        N = self.get_num_params()
        cfg = self.config
        L, H, Q, T = cfg.n_layer, cfg.n_head, cfg.n_embd//cfg.n_head, cfg.block_size
        flops_per_token = 6*N + 12*L*H*Q*T
        flops_per_fwdbwd = flops_per_token * T
        flops_per_iter = flops_per_fwdbwd * fwdbwd_per_iter
        # express our flops throughput as ratio of A100 bfloat16 peak flops
        flops_achieved = flops_per_iter * (1.0/dt) # per second
        flops_promised = 312e12 # A100 GPU bfloat16 peak flops is 312 TFLOPS
        mfu = flops_achieved / flops_promised
        return mfu

    @torch.no_grad()
    def generate(self, idx, max_new_tokens, temperature=1.0, top_k=None):
        for _ in range(max_new_tokens):
            idx_cond = idx if idx.size(1) <= self.config.block_size else idx[:, -self.config.block_size:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :] / temperature
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = -float('Inf')
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx

