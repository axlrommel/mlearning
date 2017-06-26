""" This module creates a model for CreveCoeur renting """

# Import classifiers and performance metrics
from sklearn import svm, metrics
from sklearn.externals import joblib

with open('dataCreveCoeur.csv') as f:
    LINES = f.read().splitlines()

NUM_FEATURES = len(LINES[0].split(',')) - 1
NUM_SAMPLES = len(LINES)

DATA = [[0 for x in range(NUM_FEATURES)]
        for y in range(len(LINES))]

RESULTS = []

for i, item in enumerate(LINES):
    sample = item.split(',')
    for j, feat in enumerate(sample):
        if j < NUM_FEATURES:
            DATA[i][j] = int(feat)
        else:
            RESULTS.append(int(feat))


TRAIN = DATA[:len(DATA)*7/10]
TEST = DATA[len(DATA)*7/10:]
TARGET = RESULTS[:len(DATA)*7/10]
EXPECTED = RESULTS[len(DATA)*7/10:]

# Create a classifier: a support vector classifier
CLASSIFIER = svm.SVC(kernel='linear')

#let's build the model
CLASSIFIER.fit(TRAIN, TARGET)

#let's see how we do:
PREDICTED = CLASSIFIER.predict(TEST)

print("Classification report for classifier %s:\n%s\n" %
      (CLASSIFIER, metrics.classification_report(EXPECTED, PREDICTED)))
print "Confusion matrix:\n%s" % metrics.confusion_matrix(EXPECTED, PREDICTED)

#joblib.dump(CLASSIFIER, 'classifierCC.pkl')




