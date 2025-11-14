import kagglehub as kh
import os
import pandas as pd
from PIL import Image
import numpy as np

# List all files
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))

# Load and inspect an image
img = Image.oppen(os.path.join)

path = kh.dataset_download("masoudnickparvar/brain-tumor-mri-dataset")
print("Path to dataset files:", path)
