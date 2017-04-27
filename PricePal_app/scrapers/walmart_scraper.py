from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

def search_walmart(search_term):
    search_url = "https://www.google.com/search?tbs=vw:l,mr:1,seller:8175035,init_ar:SgVKAwiUA0oKUggI-6IrIJGjK0oKUggIm8EuIJzBLg%3D%3D&tbm=shop&q="
    search = search_url + search_term
    doc = requests.get(search, headers=headers)
    soup = BeautifulSoup(doc.content, "html.parser")

    title_object = soup.find("a", {"class": "pstl"})
    title = title_object.contents[0]


    price_object = soup.find("span", {"class": "price"})
    price = price_object.contents[0].contents[0]


    return [price,title]

