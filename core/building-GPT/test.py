

with open("/Users/kaveeshtata/Projects/AI-workspace/core/tokenizer-GPT/regex_model/regex_tokenizer.model", "rb") as f:
    model = f.read()

with open("/Users/kaveeshtata/Projects/AI-workspace/core/tokenizer-GPT/regex_model/regex_tokenizer.vocab", "r", encoding="utf-8") as f:
    vocab = {}
    for line in f:
        line = line.strip()
        if not line:
            continue
        token, idx = line.rsplit(" ", 1)
        idx = int(idx)
        vocab[idx] = token.encode("utf-8")
    print(vocab)