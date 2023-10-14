# Results

## StableLM-Tuned-Alpha-3B
* Painfully slow and resource intensive, on a 16 GB RAM Intel i7 6600 Microsoft Surface Book with Cuda enabled NVIDIA GTX 965M (10GB GPU Memory, 2GB dedicated) and SSD drive (R/W ~630GB/s). 

* 5 minutes before showing prompt. 5 additional minutes before reply at 128 additional tokens. At 16 tokens, no sampling and no temperature approximately 90 seconds before reply. Runs on the GPU.

* Not maxing out on the RAM (12GB) or GPU (7.4 GB), though RAM, SSD and CPU max out on loading the shards (before replying to the prompt). 

* Replies are not very impressive.

## GPT2 
* Runs fast, though not on the GPU. Complete imbecil. Needs further fine-tuning.

## GPT-Neo 1.3B
* Runs twice as slow as GPT2, also not on the GPU. And, unfortunately, also complete imbecil. Needs further fine-tuning.

## ImageToTextGPT2
* Not at all as descriptive as I would need.