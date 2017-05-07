from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join, abspath
# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

MY_BIRDS_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/birds"
MY_NON_BIRDS_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/noBirds"
MY_CTRL_BIRDS_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/ctrlBirds"
MY_CTRL_NON_BIRDS_PATH = "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/ctrlNoBirds"

IMAGE_ROWS = 128
IMAGE_COLS = 128


def b_and_w(image_array):
    """Returns a 0 if a pixel is [0,0,0] and 1 otherwise."""
    numrows = len(image_array)
    numcols = len(image_array[0])
    newar = [[0 for x in range(numrows)] for y in range(numcols)]

    i = 0
    for each_row in image_array:
        j = 0
        for each_pix in each_row:
            if each_pix[0] != 0 or each_pix[1] != 0 or each_pix[2] != 0:
                newar[i][j] = 1
            j = j + 1
        i = i + 1
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

k = 0
j = 0
for i in range(len(BIRD_FILES)):
    im = Image.open(BIRD_FILES[j])
    im = im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
    im = im.convert("RGB")
    iar = np.array(im)
    iar = b_and_w(iar)
    iar1 = turn_to_single_array(iar)
    m = 0
    for l in range(len(iar1)):
        DATA[k][m] = iar1[m]
        m = m + 1
    k = k + 1
    j = j + 1

j = 0
for i in range(len(NON_BIRD_FILES)):
    im = Image.open(NON_BIRD_FILES[j])
    im = im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
    im = im.convert("RGB")
    iar = np.array(im)
    iar = b_and_w(iar)
    iar1 = turn_to_single_array(iar)
    m = 0
    for l in range(len(iar1)):
        DATA[k][m] = iar1[m]
        m = m + 1
    k = k + 1
    j = j + 1

# populate the samples double array
PREDICT_BIRDS = [[
    0 for x in range(IMAGE_ROWS * IMAGE_COLS)
] for y in range(len(CTRL_BIRD_FILES) + len(CTRL_NON_BIRD_FILES))]

k = 0
j = 0
for i in range(len(CTRL_BIRD_FILES)):
    im = Image.open(CTRL_BIRD_FILES[j])
    im = im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
    im = im.convert("RGB")
    iar = np.array(im)
    iar = b_and_w(iar)
    iar1 = turn_to_single_array(iar)
    m = 0
    for l in range(len(iar1)):
        PREDICT_BIRDS[k][m] = iar1[m]
        m = m + 1
    k = k + 1
    j = j + 1

j = 0
for i in range(len(CTRL_NON_BIRD_FILES)):
    im = Image.open(CTRL_NON_BIRD_FILES[j])
    im = im.resize((IMAGE_ROWS, IMAGE_COLS), Image.NEAREST)
    im = im.convert("RGB")
    iar = np.array(im)
    iar = b_and_w(iar)
    iar1 = turn_to_single_array(iar)
    m = 0
    for l in range(len(iar1)):
        PREDICT_BIRDS[k][m] = iar1[m]
        m = m + 1
    k = k + 1
    j = j + 1

EXPECTED = []
for i in range(len(CTRL_BIRD_FILES)):
    EXPECTED.append(1)
for i in range(len(CTRL_NON_BIRD_FILES)):
    EXPECTED.append(0)

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(DATA, TARGET)

#expected = [1 for x in range(len(CTRL_BIRD_FILES))]
predicted = classifier.predict(PREDICT_BIRDS)

print("Classification report for classifier %s:\n%s\n" %
      (classifier, metrics.classification_report(EXPECTED, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(EXPECTED, predicted))
#print(iar1)
#plt.imshow(iar)
#plt.show()
