from django.contrib import admin
from .models import Managers, Books


class ManagersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',)


class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'name',)

admin.site.register(Managers, ManagersAdmin)
admin.site.register(Books, BooksAdmin)
