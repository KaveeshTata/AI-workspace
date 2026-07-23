import torch
import torch.nn.functional as F

g = torch.Generator().manual_seed(2147483647)


def stoi_func():
    words = open("names.txt", 'r').read().splitlines()
    chars = sorted(list(set(''.join(words))))
    stoi = {s:i+1 for i,s in enumerate(chars)}
    stoi["."] = 0
    return stoi

stoi = stoi_func()
itos = {i: s for s, i in stoi.items()}

def initialize_data(words):
    xs, ys = [], []
    for w in words:
        chs = ["."] + list(w) + ["."]
        for ch1, ch2 in zip(chs, chs[1:]):
            ix1 = stoi[ch1]
            ix2 = stoi[ch2]
            xs.append(ix1)
            ys.append(ix2)

    xs = torch.tensor(xs)
    ys = torch.tensor(ys)
    elements = xs.nelement()

    return xs, ys, elements


def training(xs, ys, elements):
    W = torch.randn((27,27), generator=g, requires_grad=True)
    for _ in range(1000):
        #Forward pass
        xenc = F.one_hot(xs, num_classes=27).float()
        logits = xenc @ W
        counts = logits.exp()
        probs = counts / counts.sum(1, keepdims=True)
        loss = -probs[torch.arange(elements), ys].log().mean()

        #backward pass
        W.grad = None
        loss.backward()

        #learning
        with torch.no_grad():
            W -= 0.01 * W.grad

    return W

def sampling(W):
    out = []
    ix = 0
    while True:
        xenc = F.one_hot(torch.tensor([ix]), num_classes=27).float()
        logits = xenc @ W
        counts = logits.exp()
        probs = counts / counts.sum(1, keepdims=True)
        ix = torch.multinomial(probs, num_samples=1, generator=g).item()
        if ix == 0:
            break
        out.append(ix)
    return ''.join([itos[i] for i in out])


def main():
    words = open("names.txt", 'r').read().splitlines()
    xs, ys, elements = initialize_data(words)
    W = training(xs, ys, elements)
    print(sampling(W))


if __name__ == "__main__":
    main()