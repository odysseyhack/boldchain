from django.urls import path

from . import views

urlpatterns = [
    path('valid', views.giftcard_valid),
]
