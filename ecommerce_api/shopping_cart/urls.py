from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shopping_cart/$', views.shopping_cart_list),
    url(r'^shopping_cart/(?P<pk>[0-9]+)/$', views.shopping_cart_detail),
]
