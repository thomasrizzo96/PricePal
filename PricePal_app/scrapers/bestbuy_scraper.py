from bs4 import BeautifulSoup
import requests
import user_agent_headers

#specify User-Agent
header_string = user_agent_headers.get_random_header()
headers = {'User-Agent': 'User-Agent ' + header_string}

def search_bestbuy(search_term):
    search_url = "https://www.google.com/search?tbs=vw:l,mr:1,seller:1311674,init_ar:SgVKAwiLAkoKUggI4o4rIO-OK0oKUggIyt45IMveOUoKUggI4Os5IOj8PQ%3D%3D&tbm=shop&q="
    search = search_url + search_term
    doc = requests.get(search, headers=headers)
    soup = BeautifulSoup(doc.content, "html.parser")


    title_object = soup.find("a", {"class": "pstl"})
    title = title_object.contents[0]

    link_object = soup.find("a", {"class": "sh-t__title"})
    print(link_object)

    price_object = soup.find("span", {"class": "price"})
    price = price_object.contents[0].contents[0]


    return [price, title]
 #title, price, link


print(search_bestbuy("iphone 7"))
