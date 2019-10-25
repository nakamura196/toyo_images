import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import json
import urllib.request
import os
from PIL import Image
import glob

import yaml

files = glob.glob("../docs/**/info.json", recursive=True)

for file in files:
    print(file)

    with open(file) as f:
        df = json.load(f)

        id = df["@id"]
        df["@id"] = id.replace("http://nakamura196.github.io/toyo_images", "https://toyo-iiif.s3.us-east-2.amazonaws.com")

        f2 = open(file, 'w')
        json.dump(df, f2)