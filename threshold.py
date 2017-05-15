""" This module creates a model for identifying bird images that were correctly filtered """
from os.path import isfile, join, dirname, basename
from os import listdir

import numpy as np
#import matplotlib.pyplot as plt

# Import classifiers and performance metrics
from sklearn import svm, metrics
from PIL import Image

MY_ROOT_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/"
MY_BIRDS_PATH = MY_ROOT_PATH + "birds"
MY_NON_BIRDS_PATH = MY_ROOT_PATH + "noBirds"
MY_CTRL_BIRDS_PATH = MY_ROOT_PATH + "ctrlBirds"
MY_CTRL_NON_BIRDS_PATH = MY_ROOT_PATH + "ctrlNoBirds"

IMAGE_ROWS = 32
IMAGE_COLS = 32

def pop_data_from_files(file_list, out_array, starting_pos_out_array):
    """Populates data array in a double array from the input files."""
    _j = 0
    _k = starting_pos_out_array
    _root = dirname(dirname(file_list[0]))
    _bname = basename(dirname(file_list[0]))
    for _i in range(len(file_list)):
        _im = Image.open(file_list[_j])
        _fname = basename(file_list[_j])
        _im = _im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
        _im = _im.convert("RGB")
        iar = np.array(_im)
        _im = _im.convert("L")
        _im.save(join(_root, "conv", _bname, _fname))
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
            if each_pix[0] != 0 or each_pix[1] != 0 or each_pix[2] != 0:
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


BIRD_FILES = [
    join(MY_BIRDS_PATH, f) for f in listdir(MY_BIRDS_PATH)
    if isfile(join(MY_BIRDS_PATH, f)) and f.endswith('.jpg')
]
NON_BIRD_FILES = [
    join(MY_NON_BIRDS_PATH, f) for f in listdir(MY_NON_BIRDS_PATH)
    if isfile(join(MY_NON_BIRDS_PATH, f)) and f.endswith('.jpg')
]
CTRL_BIRD_FILES = [
    join(MY_CTRL_BIRDS_PATH, f) for f in listdir(MY_CTRL_BIRDS_PATH)
    if isfile(join(MY_CTRL_BIRDS_PATH, f)) and f.endswith('.jpg')
]
CTRL_NON_BIRD_FILES = [
    join(MY_CTRL_NON_BIRDS_PATH, f) for f in listdir(MY_CTRL_NON_BIRDS_PATH)
    if isfile(join(MY_CTRL_NON_BIRDS_PATH, f)) and f.endswith('.jpg')
]

#initialize the target array
TARGET = []
for i in range(len(BIRD_FILES)):
    TARGET.append(1)
for i in range(len(NON_BIRD_FILES)):
    TARGET.append(0)

# populate the samples double array
DATA = [[0 for x in range(IMAGE_ROWS * IMAGE_COLS)]
        for y in range(len(BIRD_FILES) + len(NON_BIRD_FILES))]

DATA = pop_data_from_files(BIRD_FILES, DATA, 0)
DATA = pop_data_from_files(NON_BIRD_FILES, DATA, len(BIRD_FILES))

# populate the samples double array
PREDICT_BIRDS = [[
    0 for x in range(IMAGE_ROWS * IMAGE_COLS)
] for y in range(len(CTRL_BIRD_FILES) + len(CTRL_NON_BIRD_FILES))]

PREDICT_BIRDS = pop_data_from_files(CTRL_BIRD_FILES, PREDICT_BIRDS, 0)
PREDICT_BIRDS = pop_data_from_files(CTRL_NON_BIRD_FILES, PREDICT_BIRDS, len(CTRL_BIRD_FILES))

EXPECTED = []
for i in range(len(CTRL_BIRD_FILES)):
    EXPECTED.append(1)
for i in range(len(CTRL_NON_BIRD_FILES)):
    EXPECTED.append(0)

# Create a classifier: a support vector classifier
CLASSIFIER = svm.SVC(gamma=0.001)

#let's build the model
CLASSIFIER.fit(DATA, TARGET)

#let's see how we do:
PREDICTED = CLASSIFIER.predict(PREDICT_BIRDS)

print("Classification report for classifier %s:\n%s\n" %
      (CLASSIFIER, metrics.classification_report(EXPECTED, PREDICTED)))
print "Confusion matrix:\n%s" % metrics.confusion_matrix(EXPECTED, PREDICTED)

