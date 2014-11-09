from django.db import models

class Language(models.Model):
    languageName = models.TextField()
    latinAlphabet = models.BooleanField(default=True)

    def __str__(self):
        return self.languageName


class Source(models.Model):
    url = models.TextField()
    language = models.ForeignKey(Language)
    name = models.TextField()
    type =  models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    language = models.ForeignKey(Language)
    source = models.ForeignKey(Source)
    text = models.TextField()
    title = models.TextField()
    wordcount = models.IntegerField(null=True, blank=True)
    url = models.TextField()
    author = models.TextField()
    pub_date = models.TextField()

    def __str__(self):
        return self.title


class WordList(models.Model):
    name = models.TextField()
    ordered = models.BooleanField(default=True)
    words = models.TextField()
    separator = models.TextField(blank=True)
    language = models.ForeignKey(Language)

    def __str__(self):
        return self.name


    def get_words(self):
        return self.words