from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'phone', 'date_joined', 'last_login', 'is_active']
    list_display_links = list_display

admin.site.register(User, UserAdmin)