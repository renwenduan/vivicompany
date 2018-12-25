from django.urls import path,re_path,include
import goods.views as views
from django.conf.urls import url
urlpatterns = [
    url('^$',views.index),
    re_path('^index$',views.index,name='index'),
    re_path('^contact$',views.contact_us,name='contact'),
    re_path('^about-us$',views.about_us,name='about-us'),
    url(r'^goods/(.*)/',views.goods_show,name='goods-show'),
    url(r'^shop$',views.shop,name='shop'),
    url(r'^details/(\d+)',views.details,name='details')
]
