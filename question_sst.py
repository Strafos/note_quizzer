import json
import os
import nltk 

filename = 'example' + '_tagged'
# os.system('cd pysupersensetagger; ./sst.sh ' + filename)

file = open('./pysupersensetagger/%s.pred.sst' %(filename))

sst_sentences = file.readlines()

sst_sentence = sst_sentences[0]
sst_sentence = sst_sentence[sst_sentence.find('{'):]
parsed_json = json.loads(sst_sentence)
# print parsed_json
tagged_words = parsed_json['words']
labels = parsed_json['labels']
lemmas = parsed_json['lemmas']
print tagged_words
print labels
print lemmas
keys = labels.keys()

idx = [key for key in keys if labels[key][1] == 'GROUP' or labels[key][1] == 'PERSON']

wh_questions = {
    0 : 'Who'
}

tagged_sentence = [tuple(tagged_word) for tagged_word in tagged_words]

def find_NPs(tagged_sentence):
    NP = 'NP: {<NN.*>*}' #This rule says that an NP chunk should be formed whenever
    cp = nltk.RegexpParser(NP)
    sentence = cp.parse(tagged_sentence)
    return sentence

sentence = find_NPs(tagged_sentence)
raw_NPs = get_NP(sentence)
NPs = [get_Words(raw_NP) for raw_NP in raw_NPs]
