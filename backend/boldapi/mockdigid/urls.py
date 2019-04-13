from django.urls import path

from . import views

urlpatterns = [
    path('authenticate', views.authenticate_digid),
    path('addtofund', views.add_to_fund),
    path('createuser', views.create_participant),
]
