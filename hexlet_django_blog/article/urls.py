from django.urls import path

from hexlet_django_blog.article import views
from .views import ArticleIndexView

urlpatterns = [
    path('', views.index),
    path('', ArticleIndexView.as_view(), name='articles_index'),
]
