## the gaol is to maximize the points
## by picking the best word from a list of words

## first the imports 
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

def find_highest_score(**kwargs):
    DATA_PATH, FILE_NAME, SCORES = kwargs['DATA_PATH'], kwargs['FILE_NAME'], kwargs['SCORES']
    data, scores = load_data(DATA_PATH, FILE_NAME, SCORES)
    letters = kwargs['letters'].lower()
    options = []
    highest_score = 0
    best_word = ''
    for word in data:
        if letters in word:
            options.append(word)
    for option in options:
        current_score = sum([scores[x] for x in option])
        if current_score > highest_score:
            best_word = option
    return option
kwargs = dict(
    DATA_PATH=DATA_PATH,
    FILE_NAME=FILE_NAME,
    SCORES=SCORES,
    letters='uu'
)
print(find_highest_score(**kwargs))



