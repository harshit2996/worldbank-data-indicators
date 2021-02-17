import csv
import json
import glob

fileList = glob.glob("*.csv")
for csvFile in fileList:
  csvfile = open(csvFile, 'r+')
  jsonfile = open('./../backend/api/fixtures/'+csvFile.rsplit('.', 1)[0]+'.json', 'w')


  read_file = csv.reader(csvfile)
  apps_data = list(read_file)

  rowcount = len(apps_data)

  print("Total rows incuding header: " + str(rowcount))

  fieldnames = apps_data[4]
  reader = csv.DictReader( csvfile, fieldnames)
  i=5
  num_years = len(apps_data[4])
  data = []

  while i< rowcount:
    data.append({
    'model': 'api.gdp', #change to the required model in the json files as per the models
    'pk': i-4,
    'fields': {  
        'country' : apps_data[i][0],
        'country_code' : apps_data[i][1],
        'indicator_name' : apps_data[i][2],
        'indicator_code' : apps_data[i][3],
      }
    })
    i = i+1

  i = 0
  rowcount = len(data)
  while i< rowcount:
    j=4
    while j <num_years:
      if fieldnames[j]!='':
        data[i]['fields'][fieldnames[j]] = apps_data[i+5][j]
      j = j + 1
    i = i + 1

  json.dump(data, jsonfile)

