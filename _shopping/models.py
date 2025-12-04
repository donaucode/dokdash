from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="items_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # image

    def __str__(self):
        return str(self.name)
        
class StorageLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="storage_locations_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Storage Location"
        verbose_name_plural = "Storage Locations"
    
    def __str__(self):
        return str(self.name)
        
        
   
class ShoppingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="shopping_lists_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    is_recurring = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Shopping List"
        verbose_name_plural = "Shopping Lists"
    
    def __str__(self):
        return str(self.name)
        
    def reset(self):
        for item in self.shopping_list_items.all():
            item.is_bought = False
            item.save()

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="recipes_created")
    created_at = models.DateTimeField(auto_now_add=True)
    shopping_list = models.OneToOneField(ShoppingList, on_delete=models.CASCADE, related_name="recipes") # acts as the ingredients too
    name = models.CharField(max_length=255)
    content = models.TextField()
    
class StorageLocationItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="storage_location_items_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, related_name="storage_location_items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="storage_location_items")
    
    amount = models.DecimalField(max_digits=10, decimal_places=1, default=1.0)
    
    class Meta:
        verbose_name = "Storage Location Item"
        verbose_name_plural = "Storage Location Items"
    
    def __str__(self):
        return f"{self.item.name}: {self.amount}" 

class ShoppingListItem(models.Model):
    class AMOUNT_UNITS(models.TextChoices):
        GRAMM = "GRAMM", "Gramm"
        MILLILITER = "MILLILITER", "Milliliter"
        TABLE_SPOONS = "TABLE_SPOONS", "Table Spoons"
        TEA_SPOONS = "TEA_SPOONS", "Tea Spoons"
        PIECES = "PIECES", "Pieces"
        PACKAGES = "PACKAGES", "Packages"
        BOTTLES = "BOTTLES", "Bottles"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="shopping_list_items_created")
    created_at = models.DateTimeField(auto_now_add=True)
    
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name="shopping_list_items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="shopping_list_items")
    
    amount = models.DecimalField(max_digits=10, decimal_places=1, default=1.0)
    amount_unit = models.CharField(max_length=255, choices=AMOUNT_UNITS.choices, default=AMOUNT_UNITS.GRAMM)
    
    is_bought = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Shopping List Item"
        verbose_name_plural = "Shopping List Items"
    
    def __str__(self):
        return f"{self.item.name}: {self.amount}"
