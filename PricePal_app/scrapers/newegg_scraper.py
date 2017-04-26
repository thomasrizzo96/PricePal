import requests
from bs4 import BeautifulSoup

newegg_search_url_beginning = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description="
newegg_search_url_end = "&bop=And&Order=BESTSELLING&PageSize=12"
##middle of url looks like this: "each+term+searched+with+a+plus+in+between"


##Specify user agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def search_product(user_description):##STARTING POINT
    product_search_url = find_search_url(user_description)
    #print product_search_url
    request = requests.get(product_search_url, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    price_div =  soup.find("div", { "class" : "item-container" })
    name_obj = soup.find("a", {"class": "item-title"})
    dollar_price = price_div.contents[5].contents[17].contents[3].contents[5].contents[3].contents[0]
    cents_price = price_div.contents[5].contents[17].contents[3].contents[5].contents[4].contents[0]
    price = '$' + str(dollar_price) + str(cents_price)
    name = name_obj.contents[1]
    url = str(name_obj)
    newURL = ''
    for i in range(0, len(url)):
        if url[i] == 'h' and url[i+1] == 't':
            while i < len(url)-1 and url[i] != '"':
                newURL += url[i]
                i += 1
            break
    return [price, name, url]


##HELPERS
def find_search_url(user_description):
    search_url = newegg_search_url_beginning
    for word in user_description.split(" "):
        search_url += word + "+"
    search_url += newegg_search_url_end
    return search_url

search_product("iphone 7")
