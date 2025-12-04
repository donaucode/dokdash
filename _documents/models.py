from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="documents_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    
    tags = models.ManyToManyField("_global.Tag", blank=True, related_name="documents_tagged")
    
    def __str__(self):
        return str(self.name)
    