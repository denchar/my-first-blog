from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.view),
    path("viewshow", views.show),
    path("viewshow2", views.show2),
]
