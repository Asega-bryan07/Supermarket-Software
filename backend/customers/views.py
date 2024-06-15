from django.shortcuts import render
from django.http import JsonResponse

def customer_list(request):
    # Your customer list logic here
    return JsonResponse({"message": "Customer list view"})

def customer_detail(request, pk):
    # Your customer detail logic here
    return JsonResponse({"message": f"Customer detail view for id {pk}"})
