from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from foreignArticleFinder.language_stats import Reader
from foreignArticleFinder.models import Article, WordList, Source
from foreignArticleFinder.crawler import Crawler


# Create your views here.
def index(request):

    return render(request, "index.html")

def article(request, article_id=-1):
    chineseReader = Reader(WordList.objects.get(pk=1))
    article = get_object_or_404(Article, pk=article_id)

    num = chineseReader.get_stats(article, 1000)

    return HttpResponse(article.title + "<br /><br />" + article.text + "<br/ ><br /><br />" + str(num) + " " + str(article.wordcount))


def articles(request):
    output = "<ul>"

    for article in Article.objects.all():
        output += "<li><a href=\"" + str(article.id) + "\"/>" + article.title + "</li>\n"

    output += "</ul>"

    return HttpResponse(output)


def sources(request):
    output = "<ul>"

    for source in Source.objects.all():
        output += "<li><a href=\"" + str(source.id) + "\"/>" + source.name + "</li>\n"

    output += "</ul>"

    return HttpResponse(output)

def source(request, source_id):
    Crawler(get_object_or_404(Source, pk=source_id)).get_articles()