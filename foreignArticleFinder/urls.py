from django.conf.urls import patterns, url

from foreignArticleFinder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.articles, name="articles index"),
    url(r'^articles/(?P<article_id>\d+)', views.article, name="article"),
    url(r'^sources/$', views.sources, name="sources index"),
    url(r'^sources/(?P<source_id>\d+)', views.source, name="source"),
    url(r'^analysis/(?P<article_id>\d+)/(?P<wordlist_id>\d+)/(?P<range>\d+)', views.analysis, name="analysis")
)
