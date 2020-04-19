from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'test/$', test, name='test'),
    url(r'giris/$', MainEnterPageView, name='main-entrance'),
]