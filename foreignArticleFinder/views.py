from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from foreignArticleFinder.models import Article, Source
from foreignArticleFinder.crawler import Crawler


# Create your views here.
def index(request):
    return render(request, "foreignArticleFinder/index.html")


def article(request, article_id=-1):
    return render(request, "foreignArticleFinder/article.html", {"article": get_object_or_404(Article, pk=article_id)})


def articles(request):
    return render(request, "foreignArticleFinder/articles.html", {"articles": Article.objects.all()})


def sources(request):
    return render(request, "foreignArticleFinder/sources.html", {"sources": Source.objects.all()})


def source(request, source_id):
    Crawler(get_object_or_404(Source, pk=source_id)).get_articles()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
