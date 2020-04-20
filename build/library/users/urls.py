from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'search/book/$', UserBookSearchView, name='search-book'),

]
