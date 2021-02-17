from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import populationSerializer, gdpSerializer, co2emissionSerializer, patentNonResSerializer, patentsResSerializer, exportsSerializer, LifeExpectancySerializer
from .models import population, gdp, co2emission, patentNonRes, patentsRes, exports, LifeExpectancy

# Create your views here.
@api_view(['GET'])
def indicators(request):
  data = [{'Indicators':'Population','route':'populationData'},{'Indicators':'GDP','route':'gdpData'},{'Indicators':'CO 2 Emmisions', 'route': 'co2emissionData' },{'Indicators':'Patents Non Residents', 'route': 'patentNonResData' },{'Indicators':'Patents Residents', 'route': 'patentsResData' },{'Indicators':'Exports', 'route': 'exportsData' },{'Indicators':'Life Expectancy', 'route': 'lifeExpectancyData' }]
  return Response(data)

@api_view(['GET','PATCH'])
def populationData(request):
  
  if(request.method == 'GET'):
    records = population.objects.all()
    serializer = populationSerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = population.objects.get(id=request.data['id'])
    serializer = populationSerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def gdpData(request):

  if(request.method == 'GET'):
    records = gdp.objects.all()
    serializer = gdpSerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = gdp.objects.get(id=request.data['id'])
    serializer = gdpSerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def co2emissionData(request):

  if(request.method == 'GET'):
    records = co2emission.objects.all()
    serializer = co2emissionSerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = co2emission.objects.get(id=request.data['id'])
    serializer = co2emissionSerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def lifeExpectancyData(request):

  if(request.method == 'GET'):
    records = LifeExpectancy.objects.all()
    serializer = LifeExpectancySerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = LifeExpectancy.objects.get(id=request.data['id'])
    serializer = LifeExpectancySerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    records = serializer.objects.get(id=request.data['id'])
    serializer = populationSerializer(records, data=request.data, partial=True)
    if serializer.serializer(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PATCH'])
def patentsResData(request):

  if(request.method == 'GET'):
    records = patentsRes.objects.all()
    serializer = patentsResSerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = patentsRes.objects.get(id=request.data['id'])
    serializer = patentsResSerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    records = serializer.objects.get(id=request.data['id'])
    serializer = populationSerializer(records, data=request.data, partial=True)
    if serializer.serializer(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET','PATCH'])
def patentNonResData(request):

  if(request.method == 'GET'):
    records = patentNonRes.objects.all()
    serializer = patentNonResSerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = patentNonRes.objects.get(id=request.data['id'])
    serializer = patentNonResSerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PATCH'])
def exportsData(request):

  if(request.method == 'GET'):
    records = exports.objects.all()
    serializer = exportsSerializer(records, many=True)
    return Response(serializer.data)
  elif(request.method == 'PATCH'):
    records = exports.objects.get(id=request.data['id'])
    serializer = exportsSerializer(records, data=request.data, partial=True)
    if serializer.is_valid(records):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)