from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Auth, Gift
from .serializer import GiftSerializer, UserSerializer
import bcrypt

@api_view(["GET"])
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    giftlist = user.gift_set.all()
    serializer = GiftSerializer(giftlist, many=True)
    print(type(serializer.data))
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
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    user = User(nickname=data["nickname"], date_of_birth=data["date_of_birth"])
    auth = Auth(email=data["email"], password=hashed, user=user)
    user.save()
    auth.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["PATCH"])
def updateUser(request, user_id):
    user = User.objects.get(id=user_id)
    auth = user.auth_set.get(user=user)
    data = request.data

    user.nickname = data.get("nickname", user.nickname)
    user.date_of_birth = data.get("date_of_birth", user.date_of_birth)
    auth.email = data.get("email", auth.email)
    oldPassword = auth.password
    auth.password = data.get("password", auth.password)
    if auth.password != oldPassword:
        auth.password = bcrypt.hashpw(auth.password.encode(), bcrypt.gensalt())

    user.save()
    auth.save()
    serialzer = UserSerializer(user)
    return Response(serialzer.data)