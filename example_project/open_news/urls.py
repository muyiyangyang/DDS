from django.conf.urls import patterns, url
from django.views.generic  import TemplateView


urlpatterns = patterns('open_news',
    url(r'^$','views.landing_page', name = 'home'),
    url(r'^logout$','views.logout', name = 'logout'),
    url(r'^luntan','views.luntan', name = 'luntan'),
    url(r'^yj','views.yj', name = 'yj'),
    url(r'^mainpage','views.mainpage', name = 'mainpage'),
    url(r'^apiclient$', TemplateView.as_view(template_name="apiclient.html")),
    #url(r'^mainpage',TemplateView.as_view(template_name="mainpage.html")),
    #url(r'^yj',TemplateView.as_view(template_name="yj.html")),
    #url(r'^luntan',TemplateView.as_view(template_name="luntan.html")),
    url(r'^hutai',TemplateView.as_view(template_name="hutai.html")),
    url(r'^today','views.today', name = 'today'),
    url(r'^month','views.month', name = 'month'),
    url(r'^week','views.week', name = 'week'),
    url(r'^zuozhe','views.zuozhe', name = 'zuozhe'),
    url(r'^search', 'views.search', name = 'search_results.html'),
    
)

