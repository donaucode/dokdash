from django.contrib import admin
from .models import Trip, Event, Activity, TripImage, TripFile, TripLink

admin.site.register(Trip)
admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(TripImage)
admin.site.register(TripFile)
admin.site.register(TripLink)
