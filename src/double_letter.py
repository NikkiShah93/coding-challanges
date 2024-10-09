## the gaol is find the letters that never appear doubled

import os
## custom module for loading
from load_data import load_data
CWD = os.getcwd()
DATA_PATH = f"{CWD}/data"
FILE_NAME = 'sowpods.txt'
SCORES = 'scores.json'

def no_double_letter(**kwargs):
    DATA_PATH, FILE_NAME, SCORES = kwargs['DATA_PATH'], kwargs['FILE_NAME'], kwargs['SCORES']
    data, scores = load_data(DATA_PATH, FILE_NAME, SCORES)
    double_letter = [l*2 for l in scores]
    seen = []
    for dl in double_letter:
        for word in data:
            if dl in word:
                seen.append(dl)
                break
    no_dubbles = set(double_letter).difference(seen)
    return no_dubbles

kwargs = dict(
    DATA_PATH=DATA_PATH,
    FILE_NAME=FILE_NAME,
    SCORES=SCORES
)

print(no_double_letter(**kwargs))