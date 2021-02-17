from django.db import models
import csv

csvfile = open('./../Downloaded Data/API_SP.POP.TOTL_DS2_en_csv_v2_1976634.csv', 'r+')
read_file = csv.reader(csvfile)
apps_data = list(read_file)
fieldnames = apps_data[4]
num_years = len(apps_data[4])-4
# Create your models here.
class gdp(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)
class co2emission(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)
class patentsRes(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)
class patentNonRes(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)
class LifeExpectancy(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)
class population(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)
class exports(models.Model):
  country = models.CharField(max_length=200)
  country_code = models.CharField(max_length=3)
  indicator_name = models.CharField(max_length=100)
  indicator_code = models.CharField(max_length=100)

j=0
while j < num_years-1:
  gdp.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  co2emission.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  patentsRes.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  patentNonRes.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  LifeExpectancy.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  population.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  exports.add_to_class(fieldnames[j+4], models.CharField(max_length=20,default='', blank=True ))
  j = j + 1 