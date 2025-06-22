from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("Phone number required")
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    phone = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone'

    objects = UserManager()

    def __str__(self):
        return self.phone
