from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email :
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'ADMIN')  # ← CORRECT
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) # PermissionsMixin
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('MERCHANT', 'Merchant (Shop Owner)'),
        ('CUSTOMER', 'Customer'),
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    is_merchant = models.BooleanField(default=False)  #Simplified role flag
    is_active = models.BooleanField(default=True) # AbstractBaseUser
    is_staff = models.BooleanField(default=False) # Manually added Field
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def save(self, *args, **kwargs):
        if self.user_type == 'MERCHANT':
            self.is_merchant = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.user_type})"
    
