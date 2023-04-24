from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import BadRequest
from django.contrib.auth.models import User
from .models import Profile, Gift
from .serializer import GiftSerializer, UserSerializer, ProfileSerializer
import bcrypt

@api_view(["GET"])
def listGifts(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    giftlist = user.gift_set.all()
    serializer = GiftSerializer(giftlist, many=True)
    # print(type(serializer.data))
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
    rawPassword = data["password"]
    #Using create_user isntead of create for automatic password hashing
    user = User.objects.create_user(username=data["username"], password=rawPassword)
    profile = Profile.objects.create(user=user, date_of_birth=data["date_of_birth"])
    serializer = UserSerializer(user)
    profileSerializer = ProfileSerializer(profile)
    return Response(profileSerializer.data)

@api_view(["PATCH"])
def updateUser(request, user_id):
    user = User.objects.get(pk=user_id)
    profile = user.profile
    data = request.data
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    profile.date_of_birth = data.get("date_of_birth", profile.date_of_birth)

    user.save()
    profile.save()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(["GET"])
def profile(request, user_id):
    #TODO show associated auth only if the user has an id token
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["POST"])
def login(request):
    data = request.data
    return

@api_view(["DELETE"])
def remove_gift(request, gift_id):
    gift = Gift.objects.get(pk=gift_id)
    if(gift):
        gift.delete()
        return Response({"id": gift_id})
    raise BadRequest('Invalid request.')


#TODO
    #LOGIN -
    #REMOVEGIFT --
    #DELETEACCOUNT
    #SHOWPROFILE --
