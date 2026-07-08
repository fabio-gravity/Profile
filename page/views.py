from django.shortcuts import render
from .models import Article
from django.shortcuts import render, get_object_or_404


def viewArticle(request):
    articles = Article.objects.all()
    return render(request,'page/index.html',{'articles': articles})

def articleDetail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'page/article_detail.html', {'article': article})
