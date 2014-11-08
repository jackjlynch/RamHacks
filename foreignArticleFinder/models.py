from django.db import models

class Language(models.Model):
    languageName = models.TextField()
    latinAlphabet = models.BooleanField(default=True)
    wordList = models.TextField()
    updateDate = models.DateTimeField('date last updated')

    def __str__(self):
        return self.languageName


class Article(models.Model):
    language = models.ForeignKey(Language)
    source = models.TextField()
    text = models.TextField()