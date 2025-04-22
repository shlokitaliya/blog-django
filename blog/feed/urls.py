from django.urls import path, include
from . import views

app_name = 'feed'

urlpatterns = [
    path("", views.index,name = "index"),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:blog_id>/like/', views.toggle_like, name='toggle_like'),
    path('blog/<int:blog_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),

]
