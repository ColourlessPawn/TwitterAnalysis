import operator
from collections import defaultdict
import json
from collections import Counter
from nltk.corpus import stopwords
from TwitterTokenizer import preprocess
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', '´', '…', '’', 'RT']
com = defaultdict(lambda : defaultdict(int))

# fname = 'python_blm.json'

with open('python_blm.json', 'r') as f:
    count_all = Counter()
    for line in f:
        if line != '\n':
            tweet = json.loads(line)
            terms_only = [term for term in preprocess(tweet['text'])
                          if term not in stop
                          and not term.startswith(('#', '@'))]

            # Build co-occurrence matrix
            for i in range(len(terms_only) - 1):
                for j in range(i + 1, len(terms_only)):
                    w1, w2 = sorted([terms_only[i], terms_only[j]])
                    if w1 != w2:
                        com[w1][w2] += 1
                        com_max = []
                        # For each term, look for the most common co-occurrent terms
                        for t1 in com:
                            t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
                            for t2, t2_count in t1_max_terms:
                                com_max.append(((t1, t2), t2_count))
                        # Get the most frequent co-occurrences
                        terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
                        print(terms_max[:5])