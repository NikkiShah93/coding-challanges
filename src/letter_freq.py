import os
import re

CWD = os.getcwd()
FILE_NAME = 'constitution.txt'
FILE_PATH = f'{os.getcwd()}\\data\\{FILE_NAME}'

## reading the content
# content = open(FILE_PATH).readlines()

## generating the letter dict
letter_dict = {}
with open(FILE_PATH) as f:
    for line in f:
        letters = set(re.sub('[^a-z]+', '',line.strip().lower()))
        for l in letters:
            if l in letter_dict:
                letter_dict[l] += line.strip().lower().count(l)
            else:
                letter_dict[l] = line.strip().lower().count(l)

## picking the top five
top_five = [(l, c) for l, c in sorted(list(letter_dict.items()),key=lambda x: x[1])[-5:]][::-1]
print(letter_dict)
print(top_five)