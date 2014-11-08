from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from foreignArticleFinder.language_stats import Reader
from foreignArticleFinder.models import Article, WordList

# Create your views here.
def index(request):

    return("index")

def article(request, article_id=-1):
    chineseReader = Reader(WordList.objects.get(pk=1))
    article = get_object_or_404(Article, pk=article_id)

    num = chineseReader.get_stats(article, 1000)

    return HttpResponse(article.title + "<br /><br />" + article.text + "<br/ ><br /><br />" + str(num) + " " + str(article.wordcount))


def articles(request):
    output = ""

    for article in Article.objects.all():
        output += "<a href=\"" + str(article.id) + "\"/>" + article.title + "\n"

    return HttpResponse(output)