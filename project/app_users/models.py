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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="projects", on_delete=models.CASCADE)
    status_choices = ['open', 'in_progress', 'completed']
    status = models.CharField(max_length=20, choices=status_choices, default='open')

    def __str__(self):
        return self.title


class Offer(models.Model):
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="freelancer", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    proposal_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    # Уникальность предложения по проекту и фрилансеру
    class Meta:
        unique_together = ('project', 'freelancer')

    def __str__(self):
        return f"Offer for '{self.project.title}' by {self.freelancer.username}, Status: {self.status}"


class Payments(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_payment", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', related_name="payments", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"payment from {self.sender} to {self.project.creator}"
