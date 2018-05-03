from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy.contrib.djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime

class Tweeter(models.Model):

    user = models.OneToOneField(User)
    following = models.ManyToManyField("self")

    @property
    def tweets(self):
        return Tweet.objects.filter(author__exact=self.id).order_by('-created')

    @property
    def suggested_friends(self):
        return Tweeter.objects.exclude(id__exact=self.id)[:3]

    def serialized(self):
        json_rep = {}
        json_rep['username'] = self.user.username
        json_rep['tweets'] = '/user/%d/tweets' % self.id
        return json_rep

class Tweet(models.Model):
    text = models.CharField(max_length=140) 
    author = models.ForeignKey(Tweeter)
    created = models.DateTimeField(auto_now=True)

    @property
    def author_user(self):
        return self.auther.user

    def __unicode__(self):
        return "%s,%s" % (self.author.username, self.text)

    def serialized(self):
        json_rep = {k:str(getattr(self,k)) for k in ('text', 'created')}
        json_rep['author'] = '/users/%d' % self.author.id
        return json_rep

class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    news_website = models.ForeignKey(NewsWebsite) 
    url = models.URLField()
    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    pointnum = models.CharField(max_length=100)
    answernum = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    zauthor = models.CharField(max_length=200)
    ftime = models.CharField(max_length=200)
    ztime = models.CharField(max_length=200)
    tnumber = models.CharField(max_length=100)
    allnumber = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200,blank=True)
    zhutinum = models.CharField(max_length=100,blank=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.title

class ArticleItem(DjangoItem):
    django_model = Article


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, NewsWebsite):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()
    
    if isinstance(instance, Article):
        if instance.checker_runtime:
            instance.checker_runtime.delete()
            
pre_delete.connect(pre_delete_handler)
