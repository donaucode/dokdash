from django.contrib import admin

from .models import Item, StorageLocation, ShoppingList, Recipe, StorageLocationItem, ShoppingListItem

admin.site.register(Item)
admin.site.register(StorageLocation)
admin.site.register(ShoppingList)
admin.site.register(StorageLocationItem)
admin.site.register(ShoppingListItem)
admin.site.register(Recipe)
