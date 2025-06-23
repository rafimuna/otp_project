from rest_framework import generics, permissions
from .models import Payout
from .serializers import PayoutSerializer

class PayoutListCreateView(generics.ListCreateAPIView):
    serializer_class = PayoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PayoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PayoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payout.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Admin will approve/reject payout (extend later)
        serializer.save()
