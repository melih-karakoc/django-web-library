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
