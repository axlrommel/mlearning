""" This module runs the model against all birds """
import sys
import json
import os
from os.path import join, basename

import numpy as np

from sklearn.externals import joblib
from PIL import Image

MY_ROOT_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/conversions"
MY_MODEL_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model"
IMAGE_ROWS = 32
IMAGE_COLS = 32

def pop_data_from_files(file_list, out_array):
    """Populates data array in a double array from the input files."""
    _j = 0
    _k = 0
    for _i in range(len(file_list)):
        _im = Image.open(file_list[_j])
        iar = np.array(_im)
        iar = b_and_w(iar)
        iar1 = turn_to_single_array(iar)
        _m = 0
        for _l in range(len(iar1)):
            out_array[_k][_m] = iar1[_m]
            _m += 1
        _k += 1
        _j += 1
    return out_array

def b_and_w(image_array):
    """Returns a 0 if a pixel is [0,0,0] and 1 otherwise."""
    numrows = len(image_array)
    numcols = len(image_array[0])
    newar = [[0 for _x in range(numrows)] for _y in range(numcols)]

    _i = 0
    for each_row in image_array:
        _j = 0
        for each_pix in each_row:
            #if each_pix[0] != 0 or each_pix[1] != 0 or each_pix[2] != 0: //for other than grayscale
            if each_pix != 0:  #grayscale
                newar[_i][_j] = 1
            _j += 1
        _i += 1
    return newar


def turn_to_single_array(image_array):
    """Returns a single array from a double array."""
    newar = []
    for each_row in image_array:
        for each_pix in each_row:
            newar.append(each_pix)
    return newar


def main(argv):
    """ main program """
    my_input_path = join(MY_ROOT_PATH, "reducedBWImages" + sys.argv[1])
    my_output_results = join(MY_MODEL_PATH, "reducedBWImages" + sys.argv[1])
    bird_files = []
    for root, dirs, files in os.walk(my_input_path):
        for f in files:
            in_fname = join(root, basename(f))
            if f.endswith('.jpg'):
                bird_files.append(in_fname)

    data = [[0 for x in range(IMAGE_ROWS * IMAGE_COLS)]
            for y in range(len(bird_files) + len(bird_files))]

    data = pop_data_from_files(bird_files, data)
    # run images against the model
    clf = joblib.load(join(MY_MODEL_PATH, 'classifier.pkl'))
    results = clf.predict(data)
    dictionary = dict(zip(bird_files, results))
    with open(my_output_results, 'w') as outfile:
        json.dump(dictionary, outfile)

if __name__ == "__main__":
    main(sys.argv[1:])