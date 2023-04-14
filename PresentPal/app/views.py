from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Auth, Gift
from .serializer import GiftSerializer, UserSerializer

@api_view(["GET"])
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    giftlist = user.gift_set.all()
    serializer = GiftSerializer(giftlist, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addGift(request, user_id):
    data = request.data
    user = User.objects.get(id=user_id)
    createdGift = user.gift_set.create(
        gift_name=data["gift_name"],
        price=data["price"],
        link=data["link"])
    serializer = GiftSerializer(createdGift)
    return Response(serializer.data)

@api_view(["POST"])
def createUser(request):
    data = request.data
    user = User(nickname=data["nickname"], date_of_birth=data["date_of_birth"])
    auth = Auth(email=data["email"], password=data["password"], user=user)
    user.save()
    auth.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)