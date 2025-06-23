from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')  # একই প্রোডাক্ট একবারই থাকবে ইউজারের কার্টে

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) for {self.user}"
