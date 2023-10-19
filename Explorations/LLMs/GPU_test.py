import torch

if torch.cuda.is_available():
     print("Cuda enabled GPU is available. ")
else:
     print("Cuda enabled GPU is not available :(\nMake sure your GPU drivers and CUDA/cuDNN are properly installed.")