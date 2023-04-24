from rest_framework import serializers
from .models import Gift, Profile
from django.contrib.auth.models import User

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gift
        fields=['gift_name', 'link']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=Profile
        fields=['user', 'date_of_birth', 'description']