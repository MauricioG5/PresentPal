from django.db import models
from django.utils import timezone

class User(models.Model):
    nickname = models.CharField(max_length=40)
    date_of_birth = models.DateTimeField()
    def __str__(self):
        return self.nickname

class Auth(models.Model):
    email = models.CharField(max_length=90)
    password = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Gift(models.Model):
    gift_name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)