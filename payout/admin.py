from django.contrib import admin
from .models import Payout

@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'method', 'status', 'requested_at']
    list_filter = ['status', 'method']
    search_fields = ['user__phone', 'account_number']
