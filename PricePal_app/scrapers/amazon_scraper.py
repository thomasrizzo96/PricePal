import requests
import re
from bs4 import BeautifulSoup
import user_agent_headers

amazon_search_url_beginning = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
##middle of url looks like this: "each+term+searched+with+a+plus+in+between"


##Specify user agent
header_string = user_agent_headers.get_random_header()
headers = {'User-Agent': 'User-Agent ' + header_string}

# price_regex = r"""(?:<span class="sx-price sx-price-large">
#                     <sup class="sx-price-currency">$</sup>
#                     <span class="sx-price-whole">)(\d+)(?:</span>
#                     <sup class="sx-price-fractional">)(\d+)</sup>
#                 </span>"""




def search_amazon(user_description):##STARTING POINT
    product_search_url = find_search_url(user_description)
    #print product_search_url
    request = requests.get(product_search_url, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    #print str(soup)

##with regex
    dollar_regex = r"""<span class="sx-price-whole">(\d+)</span>"""  ##ask Vladimir about the occult mysteries of regular expressions
    cents_regex = r"""<sup class="sx-price-fractional">(\d+)</sup>"""

    dollar_search = re.search(dollar_regex, str(soup))
    cents_search = re.search(cents_regex, str(soup))
    dollar_price = dollar_search.group(1)
    cents_price = cents_search.group(1)
    price = str(dollar_price) + "." + str(cents_price)


#with Beautiful Soup
    name_div =  soup.find("a", { "class" : "a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal" })
    product_name = name_div.contents[0].contents[0]

# with Beautiful Soup
    product_link_div = soup.find("div", {"class": "a-row a-spacing-none"})
    product_link_container = product_link_div.find_all('a', href=True)
    product_link = product_link_container[0]['href']

#with Beautiful Soup
    img_div = soup.find("a", { "class" : "a-link-normal a-text-normal" })
    img_src_container = img_div.find_all('img', src=True)
    try:
        img_address =  img_src_container[0]['src']
    except IndexError:
        img_address = "None"

    return_list = [price, product_name, product_link, img_address]
    #print return_list
    return return_list


##HELPERS
def find_search_url(user_description):
    search_url = amazon_search_url_beginning
    for word in user_description.split(" "):
        search_url += word + "+"
    return search_url
