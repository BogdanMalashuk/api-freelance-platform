from django.db import models
from api.api import settings


class Payments(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="payments", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', related_name="payments", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"payment from {self.sender} to {self.project.creator}"
