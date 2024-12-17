from django.shortcuts import render

def index(request):
    app_name = 'hexlet_django_blog.article'
    return render(request, 'articles/index.html', context={'app_name': app_name})
