from app.views import *
from django.urls import path
urlpatterns=[
    path("",Home,name="Home"),
    path("about/",about,name="about")
]