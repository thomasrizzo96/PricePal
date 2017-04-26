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
    bestbuy_price = search_bestbuy(product.get_name())
    ebay_data = search_ebay(product.get_name())
    ebay_price = ebay_data[2]
    ebay_name = ebay_data[0]
    ebay_image = ebay_data[1]
    walmart_price = search_walmart(product.get_name())
    newegg_data = search_product(product.get_name())
    newegg_price = newegg_data[0]
    newegg_name = newegg_data[1]
    newegg_url = newegg_data[2]
    amazon_dat = search_amazon(product.get_name())
    amazon_name = amazon_dat[0]
    amazon_price = amazon_dat[1]
    amazon_url = amazon_dat[2]
    amazon_image = amazon_dat[3]
    product.delete()
    return render(request, 'PricePal_app/results.html', {'amazon_name': amazon_name, 'amazon_price': amazon_price, 'amazon_url': amazon_url, 'amazon_image': amazon_image, 'bestbuy_price': bestbuy_price, 'ebay_price': ebay_price, 'ebay_image': ebay_image, 'ebay_name': ebay_name, 'walmart_price': walmart_price, 'newegg_price': newegg_price, 'newegg_name': newegg_name, 'newegg_url': newegg_url})
