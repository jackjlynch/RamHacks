from django.conf.urls import patterns, url

from foreignArticleFinder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.articles, name="articles index"),
    url(r'^articles/(?P<article_id>\d+)', views.article, name="article")
)
