""" This module creates a model for spam detection """

# Import classifiers and performance metrics
from sklearn import svm, metrics
from sklearn.externals import joblib

with open('allFeatures.txt') as f:
    LINES = f.read().splitlines()

with open('allResults.txt') as f:
    RLINES = f.read().splitlines()

NUM_FEATURES = len(LINES[0].split(' ')) - 1
NUM_SAMPLES = len(LINES)

DATA = [[0 for x in range(NUM_FEATURES)]
        for y in range(len(LINES))]
RESULTS = []

# read data set
for i, item in enumerate(LINES):
    sample = item.strip().split(' ')
    for j, feat in enumerate(sample):
        DATA[i][j] = int(feat)

# read the results: 1 is spam, 0 is not spam
for i, item in enumerate(RLINES):
    RESULTS.append(int(item.strip()))

#train set: first 70%
TRAIN = DATA[:len(DATA)*7/10]
TARGET = RESULTS[:len(DATA)*7/10]

#test set: last 30%
TEST = DATA[len(DATA)*7/10:]
EXPECTED = RESULTS[len(DATA)*7/10:]

# Create a classifier: a support vector classifier
LINEAR_CLASSIFIER = svm.SVC(kernel='linear')

#let's build the model
LINEAR_CLASSIFIER.fit(TRAIN, TARGET)

#let's see how we do:
PREDICTED = LINEAR_CLASSIFIER.predict(TEST)

print("Classification report for classifier %s:\n%s\n" %
      (LINEAR_CLASSIFIER, metrics.classification_report(EXPECTED, PREDICTED)))
print "Confusion matrix:\n%s" % metrics.confusion_matrix(EXPECTED, PREDICTED)

# let's save our model in a file
joblib.dump(LINEAR_CLASSIFIER, 'classifierSpam.linkl')

# Create a classifier: a support vector classifier
RBF_CLASSIFIER = svm.SVC(kernel='rbf')

#let's build the model
RBF_CLASSIFIER.fit(TRAIN, TARGET)

#let's see how we do:
PREDICTED = RBF_CLASSIFIER.predict(TEST)

print("Classification report for classifier %s:\n%s\n" %
      (RBF_CLASSIFIER, metrics.classification_report(EXPECTED, PREDICTED)))
print "Confusion matrix:\n%s" % metrics.confusion_matrix(EXPECTED, PREDICTED)

# let's save our model in a file
joblib.dump(RBF_CLASSIFIER, 'classifierSpam.rbfkl')


