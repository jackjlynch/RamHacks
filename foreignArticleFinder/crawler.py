import feedparser
from foreignArticleFinder.models import Source, Article, Language
import foreignArticleFinder.language_stats


class Crawler():
    def __init__(self, source):
        self.source = source

    def get_articles(self):
        reader = foreignArticleFinder.language_stats.Reader(self.source.language)
        if self.source.type == "rss":
            for article in  feedparser.parse(self.source.url)["entries"]:
                if not Article.objects.filter(title=article['title']).exists():
                    article = Article(language=self.source.language, source=self.source, text=article['summary_detail']['value'], title=article['title'], author=article['author'], url=article['link'], pub_date=article['published'])
                    article.wordsIn500 = reader.get_stats(article, 500)
                    article.wordsIn1000 = reader.get_stats(article, 1000)
                    article.wordsIn1500 = reader.get_stats(article, 1500)
                    article.wordsIn2000 = reader.get_stats(article, 2000)
                    article.save()