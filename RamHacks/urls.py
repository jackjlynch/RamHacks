from django.conf.urls import patterns, include, url
from django.contrib import admin
from RamHacks import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RamHacks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^finder/', include('foreignArticleFinder.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


#static files
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )