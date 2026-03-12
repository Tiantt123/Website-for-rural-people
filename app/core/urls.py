from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health, name="health"),
    path("farming/", views.farming, name="farming"),
    path("education/", views.education, name="education"),
    path("emergency/", views.emergency, name="emergency"),
]