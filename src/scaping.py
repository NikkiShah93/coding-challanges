## the goal is to find image urls
## and download the images for furthur analysis

import os
import urllib.request as request
from bs4 import BeautifulSoup
import json

response = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=10").read()
content = json.loads(response)

for row in content:
    print(row.keys())
    print()
