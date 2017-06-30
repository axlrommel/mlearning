""" checks an email to see if it's spam, reads a index 1 based file """

import sys
from sklearn.externals import joblib
NUM_FEATURES = 1899

def main(argv):
    """ main program """
    my_input_path = sys.argv[1]
    with open(my_input_path) as f:
        rlines = f.read().splitlines()

    data = [[0 for i in range(NUM_FEATURES)]for y in range(1)]

    for i, item in enumerate(rlines):
        data[0][int(item.strip())-1] = 1 #input data starts with an index of 1

    # run images against the model
    clf = joblib.load('classifierSpam.pkl')
    results = clf.predict(data)
    print results


if __name__ == "__main__":
    main(sys.argv[1:])