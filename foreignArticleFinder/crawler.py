import feedparser
from foreignArticleFinder.models import Source, Article


class Crawler():
    def __init__(self, source):
        self.source = source

    def get_articles(self):
        if self.source.type == "rss":
            for article in  feedparser.parse(self.source.url)["entries"]:
                if not Article.objects.filter(title=article['title']).exists():
                    Article(language=self.source.language, source=self.source, text=article['summary_detail']['value'], title=article['title'], author=article['author'], url=article['link'], pub_date=article['published']).save()