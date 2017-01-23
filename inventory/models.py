from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)
	parent = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)
	def __str__(self):
		return self.name

#class ItemType(models.Model):
#	name = models.CharField(max_length=50)
#	category = models.ForeignKey(ItemCategory)

class Item(models.Model):
	category = models.ForeignKey(Category, models.PROTECT)
	name = models.CharField(max_length=100)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)
	purchased = models.DateField(blank=True)
	image = models.ImageField(upload_to='itemimages/', blank=True)
	parent = models.ForeignKey('self', models.PROTECT, blank=True, null=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.name
