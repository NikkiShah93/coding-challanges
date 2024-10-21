## the goal is to find image urls
## and download the images for furthur analysis

import os
import urllib.request as request
from bs4 import BeautifulSoup
import json

CWD = os.getcwd()
DATA_PATH = f"{CWD}/data/img/"

response = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=10").read()
content = json.loads(response)

for row in content:
    if "url" in row:
        img_url = row.get("url")
        print(f"working on {img_url}")
        image_content = request.urlopen(img_url).read()
        title = row.get('title', "no_title").strip().replace(" ", "_")
        img_type = img_url.split('.')[-1] if "." in img_url else ".jpg"
        ## writing the binary to disk
        with open(f"{DATA_PATH}{title}.{img_type}", 'wb') as img:
            img.write(image_content)
            print(f"{DATA_PATH}{title}.{img_type} is written!")
        
        
