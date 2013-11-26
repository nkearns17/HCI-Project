from django.conf.urls import patterns, url
from theGames import views

# regEx ^$ matches a string thats empty.

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^events', views.events, name='events'),
	url(r'^specificEvent/(?P<event_name>\w+)', views.specific_Event, name='specificEvent'),
	url(r'^details', views.details, name='event-details'),
	url(r'^results', views.results, name='results'),
	url(r'^updates', views.updates, name='updates'),
	url(r'^selectCountry', views.selectCountry, name='selectCountry'),
)
