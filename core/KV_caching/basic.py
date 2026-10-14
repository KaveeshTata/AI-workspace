import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, DynamicCache
from accelerate import Accelerator

device = Accelerator().device

model_id = "microsoft/Phi-3-mini-4k-instruct"
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map=device)
tokenizer = AutoTokenizer.from_pretrained(model_id)

past_key_values = DynamicCache(config=model.config)
print(past_key_values)
messages = [{"role": "user", "content": "Hello, what's your name."}]
print(messages)
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
print(inputs.attention_mask)

generated_ids = inputs.input_ids
max_new_tokens = 10

for _ in range(max_new_tokens):
    outputs = model(**inputs, past_key_values=past_key_values, use_cache=True)
    # Greedily sample one next token
    next_token_ids = outputs.logits[:, -1:].argmax(-1)
    generated_ids = torch.cat([generated_ids, next_token_ids], dim=-1)
    # Prepare inputs for the next generation step by leaving unprocessed tokens, in our case we have only one new token
    # and expanding attn mask for the new token, as explained above
    attention_mask = inputs["attention_mask"]
    attention_mask = torch.cat([attention_mask, attention_mask.new_ones((attention_mask.shape[0], 1))], dim=-1)
    inputs = {"input_ids": next_token_ids, "attention_mask": attention_mask}

print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
"[INST] Hello, what's your name. [/INST]  Hello! My name is LLaMA,"