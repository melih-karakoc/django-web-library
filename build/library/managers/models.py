from django.db import models
from ..profiles.models import Profiles


class Managers(models.Model):
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE,
                                   )
    username = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=50)
    manager = models.BooleanField(default=True)
