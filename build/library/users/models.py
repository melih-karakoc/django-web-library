from django.db import models
from ..profiles.models import Profiles
from isbn_field import ISBNField


class Users(models.Model):
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE,)
    user = models.BooleanField(default=True)

    @property
    def username(self):
        return '{}'.format(self.profile.username)


    @property
    def password(self):
        return '{}'.format(self.profile.password)


class Books(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,
                             related_name='book')
    name = models.CharField(max_length=255, null=True, blank=True)
    isbn_no = ISBNField(blank=False, null=False)
    receiving_date = models.DateTimeField(blank=False, null=False)
    delivery_date = models.DateTimeField(blank=True, null=True)
