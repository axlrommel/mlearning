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

    # run emails against the rbf model
    clf = joblib.load('classifierSpam.rbfkl')
    results = clf.predict(data)
    if results[0] == 0:
        print "RBF: Not Spam"
    else:
        print "RBF:Spam"

    # run emails against the linear model
    clf1 = joblib.load('classifierSpam.linkl')
    results = clf1.predict(data)
    if results[0] == 0:
        print "Linear: Not Spam"
    else:
        print "Linear: Spam"


if __name__ == "__main__":
    main(sys.argv[1:])