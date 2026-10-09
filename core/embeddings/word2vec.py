#Refer https://github.com/OlgaChernytska/word2vec-pytorch

import torch.nn as nn
import torch
from tokenizer_GPT.regex_tokenizer import RegexTokenizer

tokenizer = RegexTokenizer()
tokenizer.load("/Users/kaveeshtata/Projects/AI-workspace/core/tokenizer_GPT/regex_model/regex_tokenizer.model")

SKIPGRAM_N_WORDS = 4
MAX_SEQUENCE_LENGTH = 256

def collate_skipgram(batch, text_tokens_ids):
    batch_input, batch_output = [], []
    for text in batch:
        if len(text_tokens_ids) < SKIPGRAM_N_WORDS * 2 + 1:
            continue

        if MAX_SEQUENCE_LENGTH:
            text_tokens_ids = text_tokens_ids[:MAX_SEQUENCE_LENGTH]

        for idx in range(len(text_tokens_ids) - SKIPGRAM_N_WORDS * 2):
            token_id_sequence = text_tokens_ids[idx : (idx + SKIPGRAM_N_WORDS * 2 + 1)]
            input_ = token_id_sequence.pop(SKIPGRAM_N_WORDS)
            outputs = token_id_sequence

            for output in outputs:
                batch_input.append(input_)
                batch_output.append(output)

    batch_input = torch.tensor(batch_input, dtype=torch.long)
    batch_output = torch.tensor(batch_output, dtype=torch.long)
    return batch_input, batch_output


class SkipgramEmbedding(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_size)

    def forward(self, input_word):
        embedded = self.embedding(input_word)
        output = self.linear(embedded)
        return output



def main():
    with open("/Users/kaveeshtata/Projects/AI-workspace/core/building-GPT/input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    ids = tokenizer.encode(text)
    batch_input, batch_output = collate_skipgram([text], ids)

    model = SkipgramEmbedding(vocab_size=tokenizer.vocab_size, embedding_dim=128)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

if __name__ == "__main__":
    main()