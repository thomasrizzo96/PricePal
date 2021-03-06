from bs4 import BeautifulSoup
import requests
import user_agent_headers

#specify User-Agent
header_string = user_agent_headers.get_random_header()
headers = {'User-Agent': 'User-Agent ' + header_string}

def search_ebay(search_term):
    #search_term.replace(" ", "+")
    search_url_half1 = "http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311.R4.TR12.TRC2.A0.H0.Xleno.TRS0&_nkw="
    search_url_half2 = "&_sacat=0"

    search_url = search_url_half1 + search_term + search_url_half2

    doc = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(doc.content, "html.parser")
    price_object = soup.find("li", {"class": "lvprice prc"})
    image_object = soup.find("div", {"class": "lvpic pic img left"})
    try:
        image = str(image_object.contents[1].contents[1].contents[1])
    except IndexError:
        image = "none"

    image = image.replace("<img", "")
    image = image.replace("/>", "")
    newImage = ""
    for i in range(0, len(image)):
        if image[i] == 'h' and image[i+1] == 't':
            while i < len(image)-1 and image[i] != '/"':
                newImage += image[i]
                i += 1
            break
    image = newImage
    name_object = soup.find("h3", {"class": "lvtitle"})
    name = name_object.contents[0].contents[0]
    price_string = price_object.contents[1].contents[0]
    price = price_string.replace("\n", "")
    price = price.replace("\t", "")

    product = [price, name, image]
    return product
