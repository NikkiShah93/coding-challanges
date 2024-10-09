## the gaol is find the all the words that have all vowels

import os
## custom module for loading
from load_data import load_data
CWD = os.getcwd()
DATA_PATH = f"{CWD}/data"
FILE_NAME = 'sowpods.txt'
SCORES = 'scores.json'

def has_all_vowels(**kwargs):
    DATA_PATH, FILE_NAME, SCORES = kwargs['DATA_PATH'], kwargs['FILE_NAME'], kwargs['SCORES']
    data, _ = load_data(DATA_PATH, FILE_NAME, SCORES)
    vowels = 'aeiou'
    vowels_list = []
    for word in data:
        if all([x in word for x in vowels]):
            vowels_list.append(word)
    return vowels_list

kwargs = dict(
    DATA_PATH=DATA_PATH,
    FILE_NAME=FILE_NAME,
    SCORES=SCORES
)

print(has_all_vowels(**kwargs)[:5])