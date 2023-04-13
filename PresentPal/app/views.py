from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Auth, Gift
from .serializer import GiftSerializer

@api_view(["GET"])
def giftlist(request, user_id):
    giftlist = Gift.objects.filter(user__id=user_id)
    serializer = GiftSerializer(giftlist, many=True)
    return Response(serializer.data)
