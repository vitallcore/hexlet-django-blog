# hexlet_django_blog/article/views.py
from django.views import View
from .models import Article
from django.shortcuts import render

class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'articles/index.html', {'articles': articles})
