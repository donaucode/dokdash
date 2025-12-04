from django.db import models
from django.contrib.auth import get_user_model
import uuid

class UserSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user_settings')
    
    # subscription
    
    does_track_task_performance = models.BooleanField(default=False)
    does_track_task_difficulty = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"
        
