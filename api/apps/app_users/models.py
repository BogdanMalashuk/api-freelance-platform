from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    login = models.CharField(max_length=50, unique=True)
    phone = models.CharField(unique=True, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Role(models.TextChoices):
        CLIENT = 'client', 'Client'
        FREELANCER = 'freelancer', 'Freelancer'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def is_client(self):
        return self.role == self.Role.CLIENT

    def is_freelancer(self):
        return self.role == self.Role.FREELANCER

    def is_admin(self):
        return self.role == self.Role.ADMIN



