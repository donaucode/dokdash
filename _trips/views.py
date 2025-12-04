from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Trip, Event, Activity, TripImage, TripFile, TripLink

def trip_read(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    
    # 1. Prefetch Activities (with their resources)
    # We sort activities by time so the timeline is correct
    activities_qs = Activity.objects.order_by('date_start', 'time_start').prefetch_related(
        'images', 
        'files', 
        'links'
    )
    
    # 2. Prefetch Events
    # Filter Event Resources: Only get images/files/links that are NOT attached to an activity
    # (activity__isnull=True)
    events = Event.objects.filter(trip=trip).order_by('date_start', 'time_start').prefetch_related(
        
        # Event Resources (Filtered)
        Prefetch('images', queryset=TripImage.objects.filter(activity__isnull=True)),
        Prefetch('files', queryset=TripFile.objects.filter(activity__isnull=True)),
        Prefetch('links', queryset=TripLink.objects.filter(activity__isnull=True)),
        
        # Activities (with their own resources already prepared above)
        Prefetch('activities', queryset=activities_qs)
    )
    
    context = {
        "trip": trip,
        "events": events,
    }
    
    return render(request, "trip_read.html", context)
    
def trip_list(request):
    pass
