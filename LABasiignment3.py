import nltk
from nltk.stem import PorterStemmer
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

ps = PorterStemmer()
paragraph = "As we have discussed before what is stemming, So it is nothing but reducing the words or chopping the words into their root forms for e.g eating becomes eat and so on. So in stemming there are different stemmers and we are going to discuss PortersStemmer the most popularly used one.Porters Stemmer It is a type of stemmer which is mainly known for Data Mining and Information Retrieval. As its applications are limited to the English language only. It is based on the idea that the suffixes in the English language are made up of a combination of smaller and simpler suffixes, it is also majorly known for its simplicity and speed. The advantage is, it produces the best output from other stemmers and has less error rate"

print(len(paragraph))
paragraph = paragraph.lower()
# stopWords = set(stopwords.words('english'))


words = word_tokenize(paragraph)
para_without_stopwords = [ w for w in words if not w in stopwords.words()]
print(para_without_stopwords)
print(len(para_without_stopwords))

for w in para_without_stopwords:
    print((ps.stem(w)))
    # print(text)
    # print(len(text))





import string;
lst = []
contents = ["shoping", "balls", "boys"]
for token in contents:
    if token.endswith('s'):
        print (token[0:-1])
    elif token.endswith("ed"):
        print (token[0:-2])
    elif token.endswith("ing"):
        print (token[0:-3])