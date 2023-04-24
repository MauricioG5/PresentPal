from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    date_of_birth = models.DateField(blank=True, null=True)
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    def __str__(self):
        return self.user.username

class Gift(models.Model):
    gift_name = models.CharField(max_length=200)
    link = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gifts')
    def __str__(self):
        return self.gift_name