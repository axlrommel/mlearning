Files in this folder:

allFeatures.txt         -- 5000x1899, every email and the words in that email, 1 = word is present, 0 = word is not present
allResults.txt          -- column vector of the results, 1 = spam, 0 = non-spam
classifierSpam.linkl    -- linear model for the spam classifier
classifierSpam.rbfkl    -- rbf model for the spam classifier
email1.idx              -- indexed words for email1. index start at 1, input for run_the_spam_model.py
email2.idx              -- indexed words for email2. index start at 1, input for run_the_spam_model.py
email3.idx              -- indexed words for email3. index start at 1, input for run_the_spam_model.py
email4.idx              -- indexed words for email4. index start at 1, input for run_the_spam_model.py
email1.txt              -- original email1
email2.txt              -- original email2
email3.txt              -- original email3
email4.txt              -- original email4
readme.txt              -- this file
run_the_spam_model.py   -- takes input a file with the indexed words, index start at 1, predicts if the email is spam or not
spamReader.py           -- reads the features and results files and creates model(s) based on them
