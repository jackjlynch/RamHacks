from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from foreignArticleFinder.models import Article, Source, Analysis, Language
from foreignArticleFinder.crawler import Crawler
from django.core import serializers
import json
from foreignArticleFinder.language_stats import Reader


# Create your views here.
def index(request):
    return render(request, "foreignArticleFinder/index.html", {"languages" : [l.languageName for l in Language.objects.all()], "ranges": [500, 1000, 1500, 2000]})


def article(request, article_id=-1):
    #return render(request, "foreignArticleFinder/article.html", {"article": get_object_or_404(Article, pk=article_id)})

    #magic
    return HttpResponse(json.dumps(json.loads(serializers.serialize("json", [get_object_or_404(Article, pk=article_id), ], fields = ("text", "author", "pub_date")))[0]))


def articles(request):
    #return render(request, "foreignArticleFinder/articles.html", {"articles": Article.objects.all()})
    return HttpResponse(serializers.serialize("json", Article.objects.all(), fields = ("title")))


def sources(request):
    return render(request, "foreignArticleFinder/sources.html", {"sources": Source.objects.all()})


def source(request, source_id):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def analysis(request, article_id, range):
    article = get_object_or_404(Article, article_id)
    reader = Reader(article.language)

    result = Analysis(article=article, language=article.language, unknownWords=reader.get_stats(article, range), range=range, wordcount=article.wordcount)