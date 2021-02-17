from rest_framework import serializers
from .models import population, gdp, co2emission, patentNonRes, patentsRes, exports, LifeExpectancy


class populationSerializer(serializers.ModelSerializer):
  class Meta:
    model = population
    fields = '__all__'

class gdpSerializer(serializers.ModelSerializer):
  class Meta:
    model = gdp
    fields = '__all__' 

class co2emissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = co2emission
    fields = '__all__' 

class patentsResSerializer(serializers.ModelSerializer):
  class Meta:
    model = patentsRes
    fields = '__all__' 

class patentNonResSerializer(serializers.ModelSerializer):
  class Meta:
    model = patentNonRes
    fields = '__all__' 

class exportsSerializer(serializers.ModelSerializer):
  class Meta:
    model = exports
    fields = '__all__' 

class LifeExpectancySerializer(serializers.ModelSerializer):
  class Meta:
    model = LifeExpectancy
    fields = '__all__' 
