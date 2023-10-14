from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList
import torch

tokenizer = AutoTokenizer.from_pretrained("StabilityAI/stablelm-tuned-alpha-3b")
model = AutoModelForCausalLM.from_pretrained("StabilityAI/stablelm-tuned-alpha-3b")
model.half().cuda()

class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [50278, 50279, 50277, 1, 0]
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False

system_prompt = """<|SYSTEM|># StableLM
- StableLM is helpful.
- StableLM is also able to write poetry, short stories, and make jokes.
"""
print("\nStableLM Tuned (Alpha version) 3B")
print("=================================")
print("\n How can I help you? (stop by entering 'exit')\n")

command = ""

while(command != "exit"):
  command = input("Prompt: ")
  if command == "exit":
    break
  prompt = f"{system_prompt}<|USER|>{command}<|ASSISTANT|>"

  inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
  tokens = model.generate(
    **inputs,
    max_new_tokens=32,
  #  temperature=0.7,
    do_sample=False,
    stopping_criteria=StoppingCriteriaList([StopOnTokens()])
  )
  reply=tokenizer.decode(tokens[0], skip_special_tokens=True)
  print(f"\n{reply[reply.find(command)+len(command):]}")