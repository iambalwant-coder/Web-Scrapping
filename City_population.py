import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://youtube.com"
req = requests.get(url)
# print(req)

soup = BeautifulSoup(req.text, "lxml")

names = soup.find_all("a",class_="style-scope ytd-rich-grid-media")

for i in names:
    print(i)