from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Auth, Gift
from .serializer import GiftSerializer

@api_view(["GET"])
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    giftlist = user.gift_set.all()
    serializer = GiftSerializer(giftlist, many=True)
    return Response(serializer.data)
