from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'is_active']
    search_fields = ['phone']
