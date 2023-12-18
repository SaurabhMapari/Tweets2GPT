import torch

print("Is CUDA available: ", torch.cuda.is_available())
print("Num GPUs Available: ", torch.cuda.device_count())
