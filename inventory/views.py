from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
	return HttpResponse(', '.join([item.name for item in Item.objects.order_by('name')]))
