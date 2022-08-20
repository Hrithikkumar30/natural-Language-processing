# # from collections import Counter
# # import pandas as pd
# # text = pd.read_txt('text.txt')
# # freq = Counter(text.split())
# # print(freq)

import nltk

# from nltk.tokenize import sent_tokenize, word_tokenize

text = open('input.txt', 'r').read()
# words = word_tokenize(text)
# print(words)

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
 
data = "The adventure turned into a nightmare. The wildness and adventure that are in fishing still recommended it to me."
stopWords = set(stopwords.words('english'))
words = word_tokenize(text)
wordsFiltered = []

for w in words:
    if w in stopWords:
        wordsFiltered.append(w)

# print(wordsFiltered)
stopWords = wordsFiltered
print(stopWords)


def stword_count(str):
    count = dict()
    
    for i in stopWords:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(stword_count(stopWords))
    
  