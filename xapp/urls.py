from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.index,name="index"),
    path("add/",views.web2,name="web2"),
]