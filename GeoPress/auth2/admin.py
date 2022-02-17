from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'phone']
    list_display_links = list_display

admin.site.register(User, UserAdmin)