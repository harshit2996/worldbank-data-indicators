from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def indicators(request):
  data = [{'Indicators':'Population'}]
  return Response(data)