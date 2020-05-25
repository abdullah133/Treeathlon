from django.shortcuts import render
from .models import Events

# Create your views here.
def eventsview(request):
    events = Events.objects.all()

    context = {'events':events,
            }
    return render(request, 'events_app/events.html', context = context)
