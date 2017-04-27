from bs4 import BeautifulSoup
import requests
import user_agent_headers

#specify User-Agent
header_string = user_agent_headers.get_random_header()
headers = {'User-Agent': 'User-Agent ' + header_string}

def search_walmart(search_term):
    search_url = "https://www.google.com/search?tbs=vw:l,mr:1,seller:8175035,init_ar:SgVKAwiUA0oKUggI-6IrIJGjK0oKUggIm8EuIJzBLg%3D%3D&tbm=shop&q="
    search = search_url + search_term
    doc = requests.get(search, headers=headers)
    soup = BeautifulSoup(doc.content, "html.parser")

    title_object = soup.find("a", {"class": "pstl"})
    if title_object:#exception checking
        title = title_object.contents[0]
    else:
        title = "No title found"

    price_object = soup.find("span", {"class": "price"})
    if price_object:
        price = price_object.contents[0].contents[0]
    else:
        price = "No price found"


    return [price,title]
