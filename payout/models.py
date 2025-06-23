from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Payout(models.Model):
    PAYMENT_METHODS = [
        ('bkash', 'Bkash'),
        ('nagad', 'Nagad'),
        ('bank', 'Bank Transfer'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payouts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    account_number = models.CharField(max_length=30)
    status = models.CharField(max_length=20, default='pending')  # pending, approved, rejected
    requested_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.phone} - {self.amount} ({self.status})"
