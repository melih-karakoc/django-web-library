from django.contrib import admin
from .models import Users, UserBooks


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'get_user_number_of_book',)


class UsersBookAdmin(admin.ModelAdmin):
    list_display = ('username', 'book_name', 'book_isbn', 'receiving_date',
                    'delivery_date',
    )

admin.site.register(Users, UsersAdmin)
admin.site.register(UserBooks, UsersBookAdmin)
