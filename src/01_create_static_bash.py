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

prefix = "http://nakamura196.github.io/toyo_images"

dir = "/Users/nakamura/git/d_toyo/toyo_images"


f = open('tmp/convert.sh', 'w')
writer = csv.writer(f, lineterminator='\n')


files = glob.glob(dir+'/gazou/**/*.jpg', recursive=True)


for file in files:
    

    opath = file.replace("/gazou/", "/docs/gazou/")

    if not os.path.exists(opath):
        print(file)
    

        tmp = os.path.split(opath)
        odir = tmp[0]

        os.makedirs(odir, exist_ok=True)

        p = odir.replace(dir+"/docs", prefix)
    
    

        line = "python iiif_static/iiif_static.py  -d "+odir+" -t 200  -p "+p+" "+file

    
        writer.writerow([line])
    

f.close()
