
from PIL import Image
import numpy as np

imgname = "C:\hobbies\AoC\AoC-Arturo\data\shreck_16pixels.bmp"
img = Image.open(imgname)   # Load image
a = np.array(img).tolist()

import json

with open("ascii_image.json","w+") as f:
    json.dump(a,f)
