from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^products/', include('products.urls')),
    url(r'^user_info/', include('user_info.urls')),
    url(r'^admin/', admin.site.urls),
]
