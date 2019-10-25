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


for i in range(len(files)):

    file = files[i]

    opath = file.replace("/gazou/", "/docs/gazou/")
    tmp = os.path.split(opath)
    odir = tmp[0]

    info_path = opath.replace(".jpg", "/info.json")

    if not os.path.exists(info_path):
        print(info_path)

        # os.makedirs(odir, exist_ok=True)

        line = "echo "+str(i+1)+"/"+str(len(files))
        writer.writerow([line])

        line = "mkdir -p "+odir
        writer.writerow([line])

        p = odir.replace(dir+"/docs", prefix)

        line = "python iiif_static/iiif_static.py  -d "+odir+" -t 200  -p "+p+" "+file
        writer.writerow([line])
    

f.close()
