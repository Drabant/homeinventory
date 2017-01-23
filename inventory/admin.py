from django.contrib import admin
from .models import Item, Category

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'parent', 'image')

admin.site.register(Item, ItemAdmin)
#admin.site.register(ItemType)
admin.site.register(Category)
