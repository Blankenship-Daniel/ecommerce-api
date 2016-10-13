from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('products.urls')),
    url(r'^', include('user_info.urls')),
    url(r'^', include('shopping_cart.urls')),
    url(r'^admin/', admin.site.urls),
]
