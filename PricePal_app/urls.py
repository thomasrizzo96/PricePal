from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index.as_view(), name='home'),
    url(r'^results/(?P<product_id>\d+)$', views.results, name='results'),






]
