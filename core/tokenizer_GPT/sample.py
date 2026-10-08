# from basic_tokenizer import BasicTokenizer

# with open("/Users/kaveeshtata/Downloads/books_large_p1.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# sample_text = text[:1_000_000]

# tokenizer = BasicTokenizer()
# tokenizer.train(
#     sample_text,
#     vocab_size=1500,
#     verbose=True
# )



from regex_tokenizer import RegexTokenizer

with open("/Users/kaveeshtata/Downloads/books_large_p1.txt", "r", encoding="utf-8") as f:
    text = f.read()

sample_text = text[:1_000_000]

tokenizer = RegexTokenizer()
tokenizer.train(
    sample_text,
    vocab_size=1500,
    verbose=True
)
tokenizer.register_special_token({
    "<BOS>": 1500,
    "<EOS>": 1501,
})

tokenizer.save("regex_tokenizer")