from django.contrib import admin
from foreignArticleFinder.models import Language, WordList, Source, Article

# Register your models here.

admin.site.register(Language)
admin.site.register(WordList)
admin.site.register(Source)
admin.site.register(Article)