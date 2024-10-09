## the gaol is find the longest palindrome

import os
## custom module for loading
from load_data import load_data
CWD = os.getcwd()
DATA_PATH = f"{CWD}/data"
FILE_NAME = 'sowpods.txt'
SCORES = 'scores.json'

def longest_palindrome(**kwargs):
    DATA_PATH, FILE_NAME, SCORES = kwargs['DATA_PATH'], kwargs['FILE_NAME'], kwargs['SCORES']
    data, _ = load_data(DATA_PATH, FILE_NAME, SCORES)
    longest_word = ''
    for word in data:
        if word == word[::-1] and len(word) > len(longest_word):
            longest_word = word
    return longest_word


kwargs = dict(
    DATA_PATH=DATA_PATH,
    FILE_NAME=FILE_NAME,
    SCORES=SCORES
)

print(longest_palindrome(**kwargs))