from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="projects", on_delete=models.CASCADE)
    status_choices = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='open')

    def __str__(self):
        return self.title


class Offer(models.Model):
    project = models.ForeignKey(Project, related_name="offers", on_delete=models.CASCADE)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="offers", on_delete=models.CASCADE)
    offer_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return f"offer for '{self.project.title}' by {self.freelancer.username}"
