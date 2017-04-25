from bs4 import BeautifulSoup
import requests


def search_bestbuy(search_term):

    search_url_half1 = "https://www.google.com/search?tbs=vw:l,mr:1,cat:267,pdtr0:706402%7C706415,pdtr1:945994%7C945995,pdtr2:947680%7C1015400,seller:1311674,init_ar:SgVKAwiLAkoKUggI4o4rIO-OK0oKUggIyt45IMveOUoKUggI4Os5IOj8PQ%3D%3D&tbm=shop&q="

    search_url = search_url_half1 + search_term

    doc = requests.get(search_url)
    soup = BeautifulSoup(doc.content, "html.parser")
    price_object = soup.find("b")
    price_string = price_object.contents[0]
    return price_string


