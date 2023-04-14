from rest_framework import serializers
from .models import User, Auth, Gift

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gift
        fields=['gift_name', 'price', 'link']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['nickname', 'date_of_birth']