import os
import random 

CWD = os.getcwd()
FILE_NAME = 'life_expectancies_usa.txt'
FILE_PATH = f'{CWD}\data\{FILE_NAME}'

## reding the file
file_content = open(FILE_PATH).readlines()

years = []
men_exp = []
women_exp = []
## parsing the file content
for row in file_content:
    year, men, women = row.strip().split(',')
    years.append(year)
    men_exp.append(men)
    women_exp.append(women)

print(years[:10])
print(men_exp[:10])
print(women_exp[:10])