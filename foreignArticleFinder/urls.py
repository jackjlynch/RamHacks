from django.conf.urls import patterns, url

from foreignArticleFinder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
