from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

command = ""

while(command != "exit"):
    command = input("Prompt: ")
    if command == "exit":
        break
    input_ids = tokenizer.encode(command, return_tensors="pt").to("cuda")
    attention_masq = torch.ones(input_ids.shape, dtype=torch.long)    
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, attention_mask=attention_masq)

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"\n{generated_text}\n")
