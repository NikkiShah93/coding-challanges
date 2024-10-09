## the gaol is find the letters that never appear doubled

import os
import json
CWD = os.getcwd()
DATA_PATH = f"{CWD}/data"
FILE_NAME = 'sowpods.txt'
SCORES = 'scores.json'
## loading the main file and the scores
def load_data(DATA_PATH, FILE_NAME, SCORES):
    with open(f'{DATA_PATH}/{FILE_NAME}') as f:
        data = f.readlines()
        ## cleaning
        data = [word.lower().strip() for word in data]
    with open(f'{DATA_PATH}/{SCORES}', 'r') as s:
        scores = json.load(s)
    return data, scores

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