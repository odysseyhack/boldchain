from django.urls import path

from . import views

urlpatterns = [
    path('authenticate', views.authenticate_digid),
]
