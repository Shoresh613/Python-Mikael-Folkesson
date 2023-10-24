# Further explorations

* Trying out the supposedly very light-weight StableLM-Tuned_Alpha-3B LLM model locally with Cuda. 
* Also tried GPT-2
* Then tried GPT-Neo
* Tried ImageToTextGPT2

## Requirements to utilize Cuda on the NVIDIA GPU

To utilize CUDA with PyTorch, you don't need a special version of PyTorch. The official PyTorch distribution supports CUDA. You need to make sure you have:

A compatible NVIDIA GPU: CUDA support requires a compatible NVIDIA GPU. Not all GPUs support CUDA, so check if your GPU is CUDA-compatible.

Install NVIDIA GPU drivers: Ensure you have the latest NVIDIA GPU drivers installed for your specific GPU. These drivers are essential for GPU support.

Install NVIDIA CUDA Toolkit: Install the NVIDIA CUDA Toolkit, which provides the necessary libraries and tools for GPU programming. You can download it from the official NVIDIA website.

Install cuDNN (CUDA Deep Neural Network library): cuDNN is a GPU-accelerated library for deep neural networks. It's often used with PyTorch to accelerate deep learning workloads. You can download it from the NVIDIA Developer website.