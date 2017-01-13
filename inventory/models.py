from django.db import models

# Create your models here.

class ItemCategory(models.Model):
	name = models.CharField(max_length=50)

class ItemType(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(ItemCategory)

class Item(models.Model):
	item_type = models.ForeignKey(ItemType)
	name = models.CharField(max_length=50)
