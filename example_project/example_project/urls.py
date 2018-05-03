from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import open_news.urls
import open_news.mobileurls
import open_news.apiurls



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example_project2.views.home', name='home'),
    # url(r'^example_project2/', include('example_project2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include(open_news.urls.urlpatterns)),
    url(r'^mobile', include(open_news.mobileurls.urlpatterns)),
    url(r'^api', include(open_news.apiurls.urlpatterns)),
    #url(r'^$', 'twitter.views.say_hello'),
    # url(r'^$', include(twitter_patterns)),
)
