from django.conf.urls import patterns, include, url
from django.contrib import admin
from RamHacks import settings
from foreignArticleFinder import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RamHacks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^finder/', include('foreignArticleFinder.urls')),
    url(r'^admin/', include(admin.site.urls)),
)