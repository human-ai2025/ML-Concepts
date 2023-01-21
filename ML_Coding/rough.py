import torch 
import torch.nn as nn

b = torch.rand(64, 256)
print(b.shape)
b = b.reshape(b.shape[0], b.shape[1], 8, b.shape[1]//8)
print(b.shape)