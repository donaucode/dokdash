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
    
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="images_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    
    tags = models.ManyToManyField("_global.Tag", blank=True, related_name="images_tagged")
    
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="files_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    
    tags = models.ManyToManyField("_global.Tag", blank=True, related_name="files_tagged")
    
class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="links_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)


class Bucket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="buckets_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    tags = models.ManyToManyField("_global.Tag", blank=True, related_name="buckets_tagged")
    
    def __str__(self):
        return f"{self.name}: {self.description}"
        
    # Bucket content
    documents = models.ManyToManyField(Document, blank=True, related_name="buckets")
    files = models.ManyToManyField(File, blank=True, related_name="buckets")
    images = models.ManyToManyField(Image, blank=True, related_name="buckets")
    links = models.ManyToManyField(Link, blank=True, related_name="buckets")

    contacts = models.ManyToManyField("_contacts.Contact", blank=True, related_name="buckets")
    shopping_lists = models.ManyToManyField("_shopping.ShoppingList", blank=True, related_name="buckets")
    recipes = models.ManyToManyField("_shopping.Recipe", blank=True, related_name="buckets")
    
    tasks = models.ManyToManyField("_tasks.Task", blank=True, related_name="buckets")
    trips = models.ManyToManyField("_trips.Trip", blank=True, related_name="buckets")
