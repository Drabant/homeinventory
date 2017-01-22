from django.db import models

# Create your models here.

class ItemCategory(models.Model):
	name = models.CharField(max_length=50)

class ItemType(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(ItemCategory)

class Item(models.Model):
	item_type = models.ForeignKey(ItemType)
	name = models.CharField(max_length=100)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)
	purchased = models.DateTimeField()
	image = models.ImageField(upload_to='itemimages/')
	parent = models.ForeignKey('self')
	description = models.TextField()
