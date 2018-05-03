# Create your views here.
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect
MOBILE_ROOT = 'mobile/'
import logging
from open_news.common_view_lib import login_view
import open_news.forms as open_newsforms
from django.shortcuts import render
from django.shortcuts import render_to_response
from open_news.models import Article
from django.http import HttpResponse
#import MySQLdb



def landing_page(request):
    if request.user.is_authenticated():
        return profile_page(request)
    else:
        return login_view(request,'', 'login.html')

@login_required(login_url='/a')
def profile_page(request):
    '''Branches actions that can be taken from the profile page'''
    if request.method == 'POST' and request.POST.get('action') == 'post_tweet':
        return _post_tweet(request)
    elif request.method == 'POST' and request.POST.get('action') == '':
        return _post_tweet(request)
    else:
        return _profile_page_get(request)

def _profile_page_get(request):
    myuser = request.user.tweeter
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-pointnum')
    return render(request,'mainpage.html', {'tweet_form': tweet_form, 'open_news_article': open_news_article,'myuser': myuser})
   
    
def _post_tweet(request):
    myuser = request.user.tweeter
    tweet_form = open_newsforms.TweetForm(request.POST)
    if tweet_form.is_valid():
        tweet_form.save()
        tweet_form = open_newsforms.TweetForm()
    return render(request,'mainpage.html', {'tweet_form': tweet_form, 'myuser': myuser})


def logout(request):
    auth.logout(request) 
    return HttpResponseRedirect('/')


def luntan(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-answernum')
    return render(request,'luntan.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})

def yj(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-ftime')
    return render(request,'yj.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})

def mainpage(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-pointnum')
    return render(request,'mainpage.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})

def today(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-pointnum')
    return render(request,'today.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})

def month(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-pointnum')
    return render(request,'month.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})

def week(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-pointnum')
    return render(request,'week.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})

def zuozhe(request):
    tweet_form = open_newsforms.TweetForm()
    open_news_article = Article.objects.order_by('-zhutinum')
    return render(request,'zuozhe.html', { 'tweet_form': tweet_form, 'open_news_article': open_news_article})




def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        open_news_article = Article.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', {  'open_news_article': open_news_article, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

