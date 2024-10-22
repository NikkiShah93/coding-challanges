## the goal is to find image urls
## and download the images for furthur analysis

import os
import urllib.request as request
from bs4 import BeautifulSoup
import json

CWD = os.getcwd()
DATA_PATH = os.path.join(CWD, "data")
IMG_PATH = os.path.join(DATA_PATH, "img")

response = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=10").read()
content = json.loads(response)

for row in content:
    if "url" in row:
        img_url = row.get("url")
        print(f"working on {img_url}")
        image_content = request.urlopen(img_url).read()
        title = row.get('title', "no_title").strip().replace(" ", "_")
        img_name = img_url.split('/')[-1] if "." in img_url else ".jpg"
        ## writing the binary to disk
        with open(f"{os.path.join(IMG_PATH,img_name)}", 'wb') as img:
            img.write(image_content)
            print(f"{img_name} is written!")
        
        
