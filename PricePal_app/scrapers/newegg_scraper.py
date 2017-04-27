import requests
from bs4 import BeautifulSoup
import user_agent_headers

newegg_search_url_beginning = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description="
newegg_search_url_end = "&bop=And&Order=BESTSELLING&PageSize=12"
##middle of url looks like this: "each+term+searched+with+a+plus+in+between"


##Specify user agent
header_string = user_agent_headers.get_random_header()
headers = {'User-Agent': 'User-Agent ' + header_string}

def search_product(user_description):##STARTING POINT
    product_search_url = find_search_url(user_description)
    #print product_search_url
    request = requests.get(product_search_url, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    price_div =  soup.find("div", { "class" : "item-container" })

    try:
        dollar_price = price_div.contents[5].contents[17].contents[3].contents[5].contents[3].contents[0]
    except IndexError:
        dollar_price = 0
    try:
        cents_price = price_div.contents[5].contents[17].contents[3].contents[5].contents[4].contents[0]
    except IndexError:
        cents_price = 0

    price = '$' + str(dollar_price) + str(cents_price)

    title_object = soup.find("a", {"class" : 'item-title'})
    if title_object:#exception checking
        title = title_object.contents[0]
        return [price, title]
    else:
        return [price, "No title found"]


##HELPERS
def find_search_url(user_description):
    search_url = newegg_search_url_beginning
    for word in user_description.split(" "):
        search_url += word + "+"
    search_url += newegg_search_url_end
    return search_url
