from django.contrib.syndication.feeds import Feed
from mysite.blog.models import BlogPost
class RSSFeed(Feed):
    title = "My awesome blog feed"
    description  "The latest from my awesome blog"
    link = "/open_news/"
    item_link = link

    def items(self):
	return BlogPost.objects.all()[:10]
