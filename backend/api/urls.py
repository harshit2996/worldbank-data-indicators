from django.urls import path
from . import views

urlpatterns = [
  path('', views.indicators, name='indicators'),
  path('populationData', views.populationData, name='populationData'),
  path('gdpData', views.gdpData, name='gdpData'),
  path('lifeExpectancyData', views.lifeExpectancyData, name='lifeExpectancyData'),
  path('exportsData', views.exportsData, name='exportsData'),
  path('patentsResData', views.patentsResData, name='patentsResData'),
  path('patentNonResData', views.patentNonResData, name='patentNonResData'),
  path('co2emissionData', views.co2emissionData, name='co2emissionData'),
]