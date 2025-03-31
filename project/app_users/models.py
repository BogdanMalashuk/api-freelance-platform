from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, unique=True)
    login = models.CharField(max_length=50, unique=True)
    phone = models.CharField(unique=True, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["first_name", "last_name", "nickname", "phone"]

    def __str__(self):
        return self.login
