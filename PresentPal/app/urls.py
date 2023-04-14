from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_id>/", views.detail, name="detail"),
    path("<int:user_id>/post/", views.addGift, name="add gift")
]