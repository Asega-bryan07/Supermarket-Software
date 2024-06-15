from django.views.generic import ListView
from django.shortcuts import render
from .models import Inventory  

class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'inventory_list' 
