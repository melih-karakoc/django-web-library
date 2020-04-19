from django.db import models
from ..profiles.models import Profiles
from isbn_field import ISBNField


class Users(models.Model):
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE,
                                   )
    username = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=50)

    user = models.BooleanField(default=True)

class Books(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,
                             related_name='book')
    name = models.CharField(max_length=255, null=True, blank=True)
    isbn_no = ISBNField(blank=False, null=False)
    receiving_date = models.DateTimeField(blank=False, null=False)
    delivery_date = models.DateTimeField(blank=True, null=True)
