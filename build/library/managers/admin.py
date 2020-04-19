from django.contrib import admin
from .models import Managers


class ManagersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',)


admin.site.register(Managers, ManagersAdmin)
