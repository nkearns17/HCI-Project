from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from theGames.models import Event, specificEvent

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('theGames/index.html', context_dict, context)

def events(request):
	template = loader.get_template('theGames/events.html')

	#request all events
	event_list = Event.objects.all()

	#put the data into the context
	context = RequestContext(request,{ 'event_list': event_list})

	return HttpResponse(template.render(context))
