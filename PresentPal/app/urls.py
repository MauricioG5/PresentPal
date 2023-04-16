from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_id>/", views.detail, name="detail"),
    path("<int:user_id>/update", views.updateUser, name="update user"),
    path("<int:user_id>/addgift/", views.addGift, name="add gift"),
    path("signup/", views.createUser, name="create user"),
]