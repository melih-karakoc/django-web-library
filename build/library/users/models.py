from django.db import models
from ..profiles.models import Profiles
from ..managers.models import Books


class Users(models.Model):
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE,)
    user = models.BooleanField(default=True)

    @property
    def username(self):
        return '{}'.format(self.profile.username)

    @property
    def password(self):
        return '{}'.format(self.profile.password)

    @property
    def get_user_number_of_book(self):
        number_book = len(self.book.all())
        return '{}'.format(number_book)


class UserBooks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,
                             related_name='book', null=True)
    # name = models.CharField(max_length=255, null=True, blank=True)
    # isbn = models.IntegerField(blank=False, null=False)
    book = models.OneToOneField(Books, on_delete=models.CASCADE, null=True)
    receiving_date = models.DateTimeField(blank=False, null=False)
    delivery_date = models.DateTimeField(blank=True, null=True)

    @property
    def username(self):
        return '{}'.format(self.user.profile.username)

    @property
    def book_name(self):
        return '{}'.format(self.book.name)

    @property
    def book_isbn(self):
        return '{}'.format(self.book.isbn)
