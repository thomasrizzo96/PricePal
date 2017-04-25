from bs4 import BeautifulSoup
import requests


def search_ebay(search_term):
    #search_term.replace(" ", "+")
    search_url_half1 = "http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311.R4.TR12.TRC2.A0.H0.Xleno.TRS0&_nkw="
    search_url_half2 = "&_sacat=0"

    search_url = search_url_half1 + search_term + search_url_half2

    doc = requests.get(search_url)
    soup = BeautifulSoup(doc.content, "html.parser")
    price_object = soup.find("li", {"class": "lvprice prc"})
    price_string = price_object.contents[1].contents[0]
    price = price_string.replace("\n", "")
    price = price.replace("\t", "")
    return price


