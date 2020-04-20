from django.contrib import admin
from .models import Managers, Books, TimeJumps


class ManagersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',)


class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'name',)


class TimeJumpAdmin(admin.ModelAdmin):
    list_display = ('day',)

admin.site.register(Managers, ManagersAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(TimeJumps, TimeJumpAdmin)
