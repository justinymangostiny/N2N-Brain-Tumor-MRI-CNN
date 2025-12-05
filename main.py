import os
import pandas as pd
from PIL import Image
import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms

train_dir = "data/Training"
test_dir = "data/Testing"

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root = train_dir, )
testset = torchvision.datasets.CIFAR10(root = test_dir)

batch_size = 4

