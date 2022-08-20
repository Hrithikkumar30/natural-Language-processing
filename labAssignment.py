from string import punctuation
import string

from pyparsing import punc8bit


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

text = open('input.txt', 'r').read()
text = text.lower()

# print(text.split())

print(word_count(text))



punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
count = 0;  
text2 = open('input.txt', 'r').read()
for i in range (0, len (text2)):   
    #Checks whether given character is a punctuation mark  
    if text2[i] in punctuation:  
        count = count + 1;  
          
print ("Total number of punctuation characters exists in file: ");  
print (count);  
