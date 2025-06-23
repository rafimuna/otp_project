from rest_framework import generics, permissions
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework import status

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # শুধু current ইউজারের কার্ট আইটেম দেখাবে
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # যদি কার্টে একই প্রোডাক্ট থাকে, quantity update করবে, নাহলে নতুন আইটেম যোগ করবে
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)
        cart_item, created = CartItem.objects.get_or_create(
            user=self.request.user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        serializer.instance = cart_item

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
