from django.db import models
from ..profiles.models import Profiles


class Managers(models.Model):
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE,
                                   )
    manager = models.BooleanField(default=True)

    @property
    def username(self):
        return '{}'.format(self.profile.username)

    @property
    def password(self):
        return '{}'.format(self.profile.password)


class Books(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.IntegerField(blank=False, null=False)


class TimeJumps(models.Model):
    day = models.IntegerField(blank=True, null=True)
