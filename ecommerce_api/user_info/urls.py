from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^billing_infos/$', views.billing_info_list),
    url(r'^shipping_infos/$', views.shipping_info_list),
    url(r'^billing_infos/(?P<pk>[0-9]+)/$', views.billing_info_detail),
    url(r'^shipping_infos/(?P<pk>[0-9]+)/$', views.shipping_info_detail),
]
