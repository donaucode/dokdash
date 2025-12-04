from django.db import models
import uuid
from django.utils.timezone import datetime

class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=510)
    
    def __str__(self):
        return self.name

# --- MIXINS ---

class TimelineMixin:
    """Logic for Dates, Times and Duration"""
    
    @property
    def effective_start(self):
        if self.date_start:
            if self.time_start:
                return datetime.combine(self.date_start, self.time_start)
            return self.date_start
        return None

    @property
    def effective_end(self):
        if self.date_end:
            if self.time_end:
                return datetime.combine(self.date_end, self.time_end)
            return self.date_end
        return None

    @property
    def has_time(self):
        return self.date_start is not None and self.time_start is not None

    @property
    def duration_display(self):
        """Returns '2.5h' or None"""
        if self.duration:
            if self.duration % 1 == 0:
                return f"{int(self.duration)}h"
            return f"{self.duration}h"
        return None

    def calculate_duration(self):
        """Internal logic to calculate hours between start and end."""
        if (self.date_start and self.time_start and 
            self.date_end and self.time_end):
            
            start = datetime.combine(self.date_start, self.time_start)
            end = datetime.combine(self.date_end, self.time_end)
            
            if end > start:
                diff = end - start
                hours = diff.total_seconds() / 3600
                self.duration = round(hours, 1)
            else:
                self.duration = 0

# --- MAIN MODELS ---

class Event(TimelineMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=510)
    
    date_start = models.DateField(blank=True, null=True)
    time_start = models.TimeField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    duration = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=1)
    
    location = models.CharField(max_length=510, blank=True, null=True)
    extra_infos = models.TextField(blank=True, null=True)
    optional = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.calculate_duration()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.trip.name} - {self.name}"

class Activity(TimelineMixin, models.Model):
    class ACTIVITY_TYPES(models.TextChoices):
        # Transport
        AIRPLANE = "AIRPLANE", "Airplane"
        CAR = "CAR", "Car"
        BUS = "BUS", "Bus"
        TRAIN = "TRAIN", "Train"
        WALK = "WALK", "Walk"
        # New Types
        MAIN = "MAIN", "Main Activity"
        WAITING = "WAITING", "Waiting / Buffer"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=255, choices=ACTIVITY_TYPES.choices)
    name = models.CharField(max_length=510)
    
    date_start = models.DateField(blank=True, null=True)
    time_start = models.TimeField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    duration = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=1)
    
    location_start = models.CharField(max_length=510, blank=True, null=True)
    location_end = models.CharField(max_length=510, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Activities"

    def save(self, *args, **kwargs):
        # 1. Auto-fill Date from Event if missing
        if not self.date_start and self.event and self.event.date_start:
            self.date_start = self.event.date_start

        # 2. Auto-calculate duration
        self.calculate_duration()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.activity_type}: {self.name}"

# --- RESOURCE MODELS ---

class TripImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
    image = models.ImageField(upload_to='trip_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = "Trip Image"
        verbose_name_plural = "Trip Images"

class TripFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="files", blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="files", blank=True, null=True)
    file = models.FileField(upload_to='trip_files/')
    name = models.CharField(max_length=255, help_text="e.g. 'Flight Ticket' or 'Menu'")
    
    class Meta:
        verbose_name = "Trip File"
        verbose_name_plural = "Trip Files"

class TripLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="links", blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="links", blank=True, null=True)
    url = models.URLField()
    title = models.CharField(max_length=255, help_text="e.g. 'Restaurant Website'")
    
    class Meta:
        verbose_name = "Trip Link"
        verbose_name_plural = "Trip Links"
    
    def __str__(self):
        return self.title
