from django.contrib.auth.models import AbstractUser
from django.db import models

from project.project import settings


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


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="projects", on_delete=models.CASCADE)
    status_choices = ['open', 'in_progress', 'completed']
    status = models.CharField(max_length=20, choices=status_choices, default='open')

    def __str__(self):
        return self.title


class Offers(models.Model):
    project = models.ForeignKey(Project, related_name="offers", on_delete=models.CASCADE)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="offers", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    proposal_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = ['pending', 'accepted', 'rejected']
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return f"Offer for {self.project.title} by {self.freelancer.username}"
