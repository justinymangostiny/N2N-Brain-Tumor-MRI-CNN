import kagglehub as kh
import os
import pandas as pd
from PIL import Image
import numpy as np

path = kh.dataset_download("masoudnickparvar/brain-tumor-mri-dataset")

# List all files
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))

# Load and inspect an image
img = Image.open(os.path.join(path, 'some_subdir', 'image_file.jpg'))
img_array = np.array(img)
print(img_array.shape)

