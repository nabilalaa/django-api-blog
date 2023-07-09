from django.urls import path
from .views import *


urlpatterns = [
    path("posts", posts),
    path("posts/<str:slug>", post),
]
