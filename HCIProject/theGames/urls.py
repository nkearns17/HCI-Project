from django.conf.urls import patterns, url
from theGames import views

# regEx ^$ matches a string thats empty.

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^events', views.events, name='events')
)
