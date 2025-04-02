from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField()
    phone = models.CharField(unique=True, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username



