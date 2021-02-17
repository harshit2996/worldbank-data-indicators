from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def indicators(request):
  data = [{'Indicators':'Population'}]
  return JsonResponse(data,safe=False)