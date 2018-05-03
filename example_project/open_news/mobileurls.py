from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^/$','open_news.mobileviews.main'),
    url('^/sign_in_success/$','open_news.mobileviews.sign_in_success'),
    url('^/sign_up_success/$','open_news.mobileviews.sign_up_success'),
    url('^/discover/$','open_news.mobileviews.discover'),
    url('/home/$','open_news.views.landing_page'),
    url('^/me/$','open_news.mobileviews.me'),
    url('^/newtweet/$','open_news.mobileviews.newtweet'),
)

