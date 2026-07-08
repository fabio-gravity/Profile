from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    path("", views.viewArticle, name='viewArticle'),
    path("article/<int:pk>/", views.articleDetail, name='articleDetail'),
]