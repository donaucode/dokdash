from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="contacts_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="as_contact_in", blank=True, null=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    
    tags = models.ManyToManyField("_global.Tag", blank=True, related_name="contacts_tagged")
    
    def __str__(self):
        return f"{self.name}: {self.description}"
        
class ContactInformation(models.Model):
    class INFORMATION_TYPES(models.TextChoices):
        GENERAL = "GENERAL", "General"
        GIFT_IDEA = "GIFT_IDEA", "Gift Idea"
        INTEREST = "INTEREST", "Interest"
        PET = "PET", "Pet"
        FEAR = "FEAR", "Fear"
        HOBBY = "HOBBY", "Hobby"
        JOB = "JOB", "Job"
        FAMILY = "FAMILY", "Family"
        CONFLICT = "CONFLICT", "Conflict"
        STATEMENT = "STATEMENT", "Statement",
        LIKES = "LIKES", "Likes"
        LIKES_NOT = "LIKES_NOT", "Likes not"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="contact_informations_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact_informations")
    information_type = models.CharField(max_length=255, choices=INFORMATION_TYPES.choices, default=INFORMATION_TYPES.GENERAL)
    content = models.TextField()
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"
    
    def __str__(self):
        return f"{self.contact.name}: {self.information_type}"
