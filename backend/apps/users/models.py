from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add extra fields later like phone number, etc.
    pass
