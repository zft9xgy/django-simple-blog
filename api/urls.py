from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes),
    path('posts/',views.getAllPosts),
    path('posts/<str:id>/',views.getPostById),

    path('tags/',views.getAllTags),
    path('tags/<str:id>/',views.getTagById),
    path('tags/<str:id>/posts/',views.getPostByTagId),
]