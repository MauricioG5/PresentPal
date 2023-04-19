from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_id>/profile", views.profile, name="show profile"),
    path("<int:user_id>/gifts", views.listGifts, name="list gifts"),
    path("<int:user_id>/update", views.updateUser, name="update user"),
    path("<int:user_id>/addgift/", views.addGift, name="add gift"),
    path("removegift/<int:gift_id>", views.remove_gift, name="remove gift"),
    path("signup/", views.createUser, name="create user"),
]