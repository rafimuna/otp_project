from rest_framework import serializers
from .models import CartItem
from products.models import Product
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # প্রোডাক্ট ডিটেইল দেখাবে

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),  # ✅ এখানে সঠিকভাবে queryset দিতে হবে
        source='product',  # এটা model field এর নাম
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']
