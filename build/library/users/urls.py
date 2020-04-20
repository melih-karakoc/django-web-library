from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'search/book/(?P<profile_id>\d+)$',
        UserBookSearchView, name='search-book'),
    url(r'take/book/(?P<profile_id>\d+)$', UserTakeBooks, name='take-book'),
    url(r'return/book/(?P<profile_id>\d+)$',
        UserReturnBookView, name='return-book'),
]
