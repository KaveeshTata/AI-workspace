from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/Phi-3-mini-4k-instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="mps",
    torch_dtype="auto",
    attn_implementation="eager",
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

print(model.eval())

prompt = """<|user|>
Write an email apologizing to Sarah for the tragic 😑 gardening mishap.
Explain how it happened.<|end|>
<|assistant|>"""

input_ids = tokenizer(
    prompt,
    return_tensors="pt"
).input_ids.to("mps")


generation_output = model.generate(
    input_ids=input_ids,
    max_new_tokens=100
)

print(
    tokenizer.decode(
        generation_output[0],
        skip_special_tokens=True
    )
)