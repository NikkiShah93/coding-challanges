## we want to see what words
## appear in the Shakespeare's sonnet
## which are missing from our scrabble list

import os
import time
## custom module for loading
from load_data import load_data
CWD = os.getcwd()
DATA_PATH = f"{CWD}/data"
FILE_NAME = 'sowpods.txt'
SCORES = 'scores.json'
SONNET = 'sonnets.txt'

def missing_words(**kwargs):
    DATA_PATH, FILE_NAME, SCORES, SONNET = kwargs['DATA_PATH'], \
        kwargs['FILE_NAME'], kwargs['SCORES'], kwargs['SONNET']
    sc_words, _ = load_data(DATA_PATH, FILE_NAME, SCORES)
    sonnet, _ = load_data(DATA_PATH, SONNET, SCORES)
    ## making a set out of the words in sonnet
    sonnet_set = set([w.strip('!.;,?:()-') for w in ' '.join(sonnet).split()])
    sc_words_set = set(sc_words)
    return sonnet_set.difference(sc_words_set)


kwargs = dict(
    DATA_PATH=DATA_PATH,
    FILE_NAME=FILE_NAME,
    SCORES=SCORES,
    SONNET=SONNET
)

start = time.time()
print(missing_words(**kwargs))
end = time.time()
print('The funtion took: ', round(end - start, 2))