import nltk
import string
import re

def get_sentences(line):
    S = []
    period_idx = [m.start() for m in re.finditer('\.', line)]
    prev_idx = 0
    for idx in period_idx:
        if prev_idx is 0:  
            S.append(line[prev_idx:idx+1])
        else:
            S.append(line[prev_idx+2:idx+1])
        prev_idx = idx
    return S


file = open('caesar_clean.txt')
raw_text = file.readlines()
text = []
for line in raw_text:
    text = text + get_sentences(line)

tokens = nltk.word_tokenize(text[0])
# print tokens
tagged_sentence = nltk.pos_tag(tokens)
print tagged_sentence