from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

class Task(models.Model):
    class STATUSES(models.TextChoices):
        OPEN = "OPEN", "Open"
        WORKING_ON = "WORKING_ON", "Working on"
        ON_HOLD = "ON_HOLD", "On Hold"
        DONE = "DONE", "Done"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="tasks_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    timebox_date_start = models.DateField(blank=True, null=True)
    timebox_time_start = models.TimeField(blank=True, null=True)
    timebox_date_end = models.DateField(blank=True, null=True)
    timebox_time_end = models.TimeField(blank=True, null=True)
    
    priority = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    difficulty = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    status = models.CharField(max_length=255, choices=STATUSES.choices, default=STATUSES.OPEN)
	
	# done_note - something to say when done
	# performance_rating - How was my performance?
    
    tags = models.ManyToManyField("_global.Tag", blank=True, related_name="tasks_tagged")
    
    def __str__(self):
        return str(self.name)