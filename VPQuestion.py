import nltk
import string
import random
import time
from Tkinter import *

def to_String(tokens):
    return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()

def find_VPs(tagged_sentence):
    VP = 'VP: {<JJ.*>*<VB.*>?<NN.*>*<POS>?<CC>?<NN.*>}' #This rule says that an VP chunk should be formed whenever 
    # VP = 'VP: {<VB.*>}'
    cp = nltk.RegexpParser(VP)
    sentence = cp.parse(tagged_sentence)
    #sentence.draw()
    return sentence

def get_VP(sentence):
    return [line for line in [str(sentence[i]) for i in range(len(sentence))] if line[1:3] == 'VP']

def get_Words(VP):
    if VP[1:3] != 'VP':
        raise Exception('Not an VP')
    space_idx = [pos + 1 for pos, char in enumerate(VP) if char == ' ']
    slash_idx = [pos for pos, char in enumerate(VP) if char == '/']
    return [VP[space_idx[i]:slash_idx[i]] for i in range(len(space_idx))]

file = open('fungi_notes.txt')
raw_text = file.readlines()
text = [line for line in raw_text if len(line) > 1 and '-----' not in line]
line_idx = [i for i in range(len(raw_text)) if len(raw_text[i]) <= 1]
note_idx = [i for i in range(len(raw_text)) if len(raw_text[i]) > 1 and '-----' in raw_text[i]]

def VP_question(num):
    tokens = nltk.word_tokenize(text[num])
    tagged_sentence = nltk.pos_tag(tokens)
    print(tagged_sentence)

    sentence = find_VPs(tagged_sentence)
    raw_VPs = get_VP(sentence)
    VPs = [get_Words(raw_VP) for raw_VP in raw_VPs]
    print VPs

    #ugly, ugly
    raw_questions = []
    banned_words = ['is', 'and', "'s"]

    for VP in VPs:
        #if "'s" in VP:
        #    idx = VP.index("'s")
        #    VP[idx - 1] += VP[idx]
        #    VP[idx] = ''
        temp = tokens[:]
        first = True
        for word in tokens:
            for VP_word in VP:
                if VP_word in temp and VP_word not in banned_words:
                    idx = temp.index(VP_word)
                    if first == True or prev_idx + 1 == idx or prev_idx + 2 == idx:
                        num_spaces = len(temp[idx])
                        temp[idx] = '_'*num_spaces
                        first = False
                    prev_idx = idx
        raw_questions.append(temp)
    for q in raw_questions:
       print to_String(q)
    # randoQ = random.randrange(len(raw_questions))
    # return to_String(raw_questions[randoQ])

for i in range(0,47):
    print i
    VP_question(i)
    a = raw_input('Enter')
# save_text = []
# def new_VP_text():
#     counter = 0
#     T.delete(1.0, END)
#     for i in range(len(text)):
#         counter = counter + 1
#         line = VP_question(i)
#         save_text.append(line + '\n')
#         T.insert(END, line + '\n')
#         if counter in line_idx:
#             counter = counter + 1
#         elif counter in note_idx:
#             T.insert(END, '----------------------------\n')
#             save_text.append('----------------------------\n')
#             counter = counter + 1

# def full_text():
#     T.delete(1.0, END)
#     [T.insert(END, line) for line in raw_text if len(line) > 1]

# def saved_VP_text():
#     T.delete(1.0, END)
#     [T.insert(END, line) for line in save_text]

# top = Tk()

# def key(event):
#     print event.char
#     if event.char is 'f': full_text()
#     if event.char is 'N': new_VP_text()
#     if event.char is 'n': saved_VP_text()
    
# #def callback(event):
#     # bop.focus_set()

# bop = Frame(top, width=100, height = 50)
# Button(bop, text='Exit', command=top.destroy).pack() #Adding a button means set_focus in while loop
# bop.focus_set()
# bop.bind("<Key>", key)
# #bop.bind("<Button-1>", callback)
# bop.pack(side=RIGHT)

# T = Text(width = 80, height = 50)
# T.pack(side=LEFT)

# def troll():
#     T.delete(1.0, END)
#     T.insert(END, 'asdasdas')

# #new_VP_text()
# while True:
#     bop.focus_set()
#     top.update_idletasks()
#     top.update()