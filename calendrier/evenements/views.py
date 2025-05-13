from django.shortcuts import render, get_object_or_404
from .models import Event
from django.utils import timezone

# Create your views here.

def index(request):
    evenements = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'evenements/index.html', {'evenements': evenements})

# def liste_evenements(request):
#     evenements = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
#     return render(request, 'evenements/liste_evenements.html', {'evenements': evenements})


def detail_evenement(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'evenements/detail_evenement.html', {'event' : event})