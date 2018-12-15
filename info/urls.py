from django.urls import path,re_path
import info.views as views
urlpatterns = [
    re_path('^$',views.index),
    path('index/',views.index),
    path('contact_us/',views.contact_us, name='contact_us')
]
