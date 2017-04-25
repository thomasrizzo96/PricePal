from bs4 import BeautifulSoup
import requests


def search_walmart(search_term):
    search_url = "https://www.google.com/search?tbs=vw:l,mr:1,seller:8175035,init_ar:SgVKAwiUA0oKUggI-6IrIJGjK0oKUggIm8EuIJzBLg%3D%3D&tbm=shop&q="
    search = search_url + search_term

    doc = requests.get(search)
    soup = BeautifulSoup(doc.content, "html.parser")
    price_object = soup.find("b")
    price = price_object.contents[0]
    return price
