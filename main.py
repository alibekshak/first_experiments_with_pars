import requests
from bs4 import BeautifulSoup
from core.config import HEADERS, URL

response = requests.get(url=URL, headers=HEADERS)
head_html = response.content


with open("core/index.html", "w", encoding="utf-8") as file:
    file.write(str(head_html))


#__________________________________________________________________________

with open("core/index.html", "r", encoding="utf-8") as file:
    content_html = file.read()

soup = BeautifulSoup(content_html, "lxml")
spin_info = soup.find_all(class_="product-carousel__img")



with open("img.html", "w", encoding="utf-8") as file:
    file.write(str(spin_info))

