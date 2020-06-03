import operator
import json
from collections import Counter
from nltk.corpus import stopwords
from TwitterTokenizer import preprocess
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', '´', '…', '’', 'RT']


fname = 'python_blm.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        if line != '\n':
            tweet = json.loads(line)
            # Create a list with all the terms
            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            # Update the counter
            count_all.update(terms_stop)
        # Print the first 5 most frequent words
    print(count_all.most_common(20))