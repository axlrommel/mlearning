"""Module to reduce image size and convert to B & W """
import os
from os.path import join, basename

from PIL import Image

MY_ROOT_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011"
MY_INPUT_PATH = join(MY_ROOT_PATH, "backInBlack")
MY_OUTPUT_PATH = join(MY_ROOT_PATH, "reducedBWImages")

IMAGE_ROWS = 32
IMAGE_COLS = 32

for root, dirs, files in os.walk(MY_INPUT_PATH):
    for f in files:
        in_fname = join(root, basename(f))
        if f.endswith('.jpg'):
            out_dir = join(MY_OUTPUT_PATH, basename(root))
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            _im = Image.open(in_fname)
            _im = _im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
            _im = _im.convert("RGB")
            _im = _im.convert("L")
            _im.save(join(out_dir, basename(f)))
