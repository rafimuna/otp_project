import random
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

@api_view(['POST'])
def send_otp(request):
    phone = request.data.get('phone')
    otp = random.randint(1000, 9999)
    cache.set(phone, otp, timeout=300)
    return Response({'message': 'OTP sent', 'otp': otp})  # frontend এ টেস্টের জন্য OTP পাঠাচ্ছি

@api_view(['POST'])
def verify_otp(request):
    phone = request.data.get('phone')
    otp = request.data.get('otp')
    real_otp = cache.get(phone)

    if str(otp) == str(real_otp):
        user, created = User.objects.get_or_create(phone=phone)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid OTP'}, status=400)
