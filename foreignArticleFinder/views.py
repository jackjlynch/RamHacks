from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from foreignArticleFinder.language_stats import Reader
from foreignArticleFinder.models import Article, WordList, Source
from foreignArticleFinder.crawler import Crawler


# Create your views here.
def index(request):
    return render(request, "foreignArticleFinder/index.html")


def article(request, article_id=-1):
    return render(request, "foreignArticleFinder/article.html", {"article": get_object_or_404(Article, pk=article_id)})


def articles(request):
    return render(request, "foreignArticleFinder/articles.html", {"articles": Article.objects.all()})


def sources(request):
    output = "<ul>"

    for source in Source.objects.all():
        output += "<li><a href=\"" + str(source.id) + "\"/>" + source.name + "</li>\n"

    output += "</ul>"

    return HttpResponse(output)

def source(request, source_id):
    Crawler(get_object_or_404(Source, pk=source_id)).get_articles()