"""Module to reduce image size and convert to B & W """
import sys
import os
from os.path import join, basename

from PIL import Image
MY_ROOT_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/conversions"

IMAGE_ROWS = 32
IMAGE_COLS = 32

def main(argv):
    """ main program """
    my_input_path = join(MY_ROOT_PATH, "backInBlack" + sys.argv[1])
    my_output_path = join(MY_ROOT_PATH, "reducedBWImages" + sys.argv[1])
    for root, dirs, files in os.walk(my_input_path):
        for f in files:
            in_fname = join(root, basename(f))
            if f.endswith('.jpg'):
                out_dir = join(my_output_path, basename(root))
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                _im = Image.open(in_fname)
                _im = _im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
                _im = _im.convert("RGB")
                _im = _im.convert("L")
                _im.save(join(out_dir, basename(f)))

if __name__ == "__main__":
    main(sys.argv[1:])
