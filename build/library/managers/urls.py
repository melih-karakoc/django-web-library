from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'add/book/(?P<profile_id>\d+)$', ImageUploadView, name='add-book'),
    url(r'user/list/(?P<profile_id>\d+)$',
        ManagerUserListView, name='user-list'),
    url(r'time/jump/(?P<profile_id>\d+)$',
        MangerTimeJumpView, name='time-jump'),
]
