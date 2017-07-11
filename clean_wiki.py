import string
import re

text = open('caesar.txt')

paragraphs = []
[paragraphs.append(paragraph) for paragraph in text]

clean_paragraph = []
gen = (paragraph for paragraph in paragraphs if len(paragraph) > 1)
for paragraph in gen:
    while '[' in paragraph:
        left, right = paragraph.find('['), paragraph.find(']')
        paragraph = paragraph[:left] + paragraph[right+1:]
    clean_paragraph.append(paragraph)

file = open('caesar_clean.txt','w')
[file.write(paragraph) for paragraph in clean_paragraph]
