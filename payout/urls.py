from django.urls import path
from .views import PayoutListCreateView, PayoutDetailView

urlpatterns = [
    path('payouts/', PayoutListCreateView.as_view(), name='payout-list-create'),
    path('payouts/<int:pk>/', PayoutDetailView.as_view(), name='payout-detail'),
]
