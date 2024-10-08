from django.contrib import admin
from .models import User, UserContacts

admin.site.register(UserContacts)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    list_display_links = ['username']
    search_fields = ['first_name']