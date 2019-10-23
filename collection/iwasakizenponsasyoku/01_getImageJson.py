import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import json
import hashlib
import os
from PIL import Image

import requests
import shutil

def download_img(url, file_name):
    print(url)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def dwn(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    
    img = soup.find("img")

    src = img.get("src")

    src = os.path.split(url)[0] + "/" + img.get("src")

    opath = src.replace("http://124.33.215.236/", "../../")

    if not os.path.exists(opath):

        tmp = os.path.split(opath)

        os.makedirs(tmp[0], exist_ok=True)

        download_img(src, opath)


url = "http://124.33.215.236/gazou/index_img_iwasakizenponsasyoku.php"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

aas = soup.find_all("a")

urls = []

for a in aas:
    href = a.get("href")
    urls.append(href)

for url0 in sorted(urls):

    if "___2009" in url0 or "/2010/" in url0:
        url1 = "http://124.33.215.236/gazou/"+url0.replace("./", "")
        print(url1)

        id = url1.split("TGName=")[1].split("&")[0]

        try:
            html = requests.get(url1).text
        except Exception as e:
            print(e)
            continue
        soup = BeautifulSoup(html, "html.parser")

        dwn(url1)

        aas = soup.find_all("a")

        for a in aas:
            href = a.get("href")
            if "_read.php" in href:
                pp = href.split("?")[0]
                url = url1.split(pp)[0] + href
                dwn(url)