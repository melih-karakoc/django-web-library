from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Profiles


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'id',)


admin.site.register(Profiles, ProfilesAdmin)