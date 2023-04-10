from django.db import models
from django.utils import timezone

class User(models.Model):
    nickname = models.CharField(max_length=40)
    date_of_birth = models.DateTimeField()
    def __str__(self):
        return self.nickname
