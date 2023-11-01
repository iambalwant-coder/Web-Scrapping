import requests
import pandas as pd 
from bs4 import BeautifulSoup

product = []
price = []
rating = []
discount = []

url = "https://www.snapdeal.com/products/electronics-headphones?sort=plrty"
req = requests.get(url)
# print(req)

soup = BeautifulSoup(req.text, "lxml")
# print(soup)

product_name = soup.find_all("p", class_ = "product-title")

for i in product_name:
    product.append(i.text)

rate = soup.find_all("span",class_="lfloat product-price")

for i in rate:
    price.append(i.text)

# like = soup.find_all("p",class_="product-rating-count")

# for i in like:
#     rating.append(i.text)

offer = soup.find_all("div",class_="product-discount")

for i in offer:
    discount.append(i.text)
# print(discount)


df = pd.DataFrame({"Product Name ":product, "Product Price ":price, "Discount":discount})
df.to_csv("snapdeal.csv")
