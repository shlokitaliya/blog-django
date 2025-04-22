from django.urls import path, include
from . import views

app_name = 'feed'

urlpatterns = [
    path("", views.index,name = "index"),


]
