from django.urls import path,re_path,include
import goods.views as views
from django.conf.urls import url
urlpatterns = [
    url('^$',views.index),
    re_path('^index$',views.index,name='index'),
    re_path('^contact_us$',views.contact_us,name='contact_us'),
    re_path('^about_us$',views.about_us,name='about_us')
]
