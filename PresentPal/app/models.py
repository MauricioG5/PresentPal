from django.db import models
from django.utils import timezone

class User(models.Model):
    nickname = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.nickname

class Auth(models.Model):
    email = models.CharField(max_length=90)
    password = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Auth for " + self.user.nickname

class Gift(models.Model):
    gift_name = models.CharField(max_length=200)
    link = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.gift_name