from django.shortcuts import render
from django.http import JsonResponse

def employee_list(request):
    # Your employee list logic here
    return JsonResponse({"message": "Employee list view"})

def employee_detail(request, pk):
    # Your employee detail logic here
    return JsonResponse({"message": f"Employee detail view for id {pk}"})
