from django.shortcuts import render
from PricePal_app.models import Product
from django.urls import reverse
from django.views.generic import CreateView

from PricePal_app.scrapers.bestbuy_scraper import search_bestbuy
from PricePal_app.scrapers.ebay_scraper import search_ebay
from PricePal_app.scrapers.walmart_scraper import search_walmart
from PricePal_app.scrapers.newegg_scraper import search_product



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
    ebay_price = search_ebay(product.get_name())
    walmart_price = search_walmart(product.get_name())
    newegg_price = search_product(product.get_name())
    product.delete()
    return render(request, 'PricePal_app/results.html', {'bestbuy_price': bestbuy_price, 'ebay_price': ebay_price, 'walmart_price': walmart_price, 'newegg_price': newegg_price})
