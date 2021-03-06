from django.shortcuts import render
from PricePal_app.models import Product
from django.urls import reverse
from django.views.generic import CreateView

from PricePal_app.scrapers.bestbuy_scraper import search_bestbuy
from PricePal_app.scrapers.ebay_scraper import search_ebay
from PricePal_app.scrapers.walmart_scraper import search_walmart
from PricePal_app.scrapers.newegg_scraper import search_product
from PricePal_app.scrapers.amazon_scraper import search_amazon



class index(CreateView):
    model = Product
    fields = ['name']
    def get_success_url(self):#redirects you to the result page
        return reverse('results', args=[self.object.id])


def loading(request):
    return render(request, 'PricePal_app/loading.html')


def results(request, product_id):
    product = Product.objects.get(id=product_id)
    product_name = product.get_name()

    bestbuy_data = search_bestbuy(product.get_name())
    bestbuy_price = bestbuy_data[0]
    bestbuy_title = bestbuy_data[1]

    ebay_data = search_ebay(product.get_name())
    ebay_price = ebay_data[0]
    ebay_title = ebay_data[1]
    ebay_image = ebay_data[2]

    walmart_data = search_walmart(product.get_name())
    walmart_price = walmart_data[0]
    walmart_title = walmart_data[1]

    newegg_data = search_product(product.get_name())
    newegg_price = newegg_data[0]
    newegg_title = newegg_data[1]

    amazon_data = search_amazon(product.get_name())
    amazon_price = amazon_data[0]
    amazon_title = amazon_data[1]
    amazon_link = amazon_data[2]
    amazon_image = amazon_data[3]

    product.delete()


    return render(request, 'PricePal_app/results.html', {'amazon_price':amazon_price,'amazon_link':amazon_link,'amazon_image':amazon_image,'amazon_title':amazon_title,'bestbuy_price': bestbuy_price,'bestbuy_title':bestbuy_title, 'ebay_price': ebay_price,'ebay_title':ebay_title,'ebay_image':ebay_image, 'walmart_price': walmart_price,'walmart_title':walmart_title, 'newegg_price': newegg_price,'newegg_title':newegg_title, 'product_name':product_name})
