from django.db import models


class Profiles(models.Model):
    full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    username = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, null=False, blank=False)
