from django.shortcuts import render
from .models import Event
from django.utils import timezone

# Create your views here.
def liste_evenements(request):
    evenements = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'evenements/liste_evenements.html', {'evenements': evenements})