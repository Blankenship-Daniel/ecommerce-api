from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shopping_carts/$', views.shopping_cart_list),
    url(r'^shopping_cart/(?P<pk>[0-9]+)/$', views.shopping_cart_detail),
    url(r'^shopping_cart_products/$', views.shopping_cart_list),
    url(r'^shopping_cart_product/(?P<pk>[0-9]+)/$', views.shopping_cart_detail),
]
