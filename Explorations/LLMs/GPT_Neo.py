from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

model_name = "EleutherAI/gpt-neo-1.3B"

# Check GPU availability
# if torch.cuda.is_available():
#     print("Cuda enabled GPU is available. Loading model to GPU ...")
#     # Initialize the model on the GPU
#     model = GPTNeoForCausalLM.from_pretrained(model_name).to('cuda')
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name).to('cuda')
# else:
    # print("GPU is not available. Make sure your GPU drivers and CUDA/cuDNN are properly installed.")
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

print("\nEleutherAI/gpt-neo-1.3B")
print("=================================")
print("\nHow can I help you? (stop by entering 'exit')\n")

command = ""

while(True):
    command = input("Prompt: ")
    if command == "exit":
        break

    # Encode the prompt
    # if torch.cuda.is_available():
    #     input_ids = tokenizer.encode(command, return_tensors="pt").to('cuda')
    # else:
    input_ids = tokenizer.encode(command, return_tensors="pt")
    # attention_masq = torch.ones(input_ids.shape, dtype=torch.long).to('cuda')    
    attention_masq = torch.ones(input_ids.shape, dtype=torch.long)    

    # Generate text
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, attention_mask=attention_masq)

    # Decode the generated text
    # generated_text = tokenizer.decode(output[0], skip_special_tokens=True).to('cuda')
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)
