import json
## loading the main file and the scores
def load_data(DATA_PATH, FILE_NAME, SCORES):
    with open(f'{DATA_PATH}/{FILE_NAME}') as f:
        data = f.readlines()
        ## cleaning
        data = [word.lower().strip() for word in data]
    with open(f'{DATA_PATH}/{SCORES}', 'r') as s:
        scores = json.load(s)
    return data, scores