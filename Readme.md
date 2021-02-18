# Application for Application to View and Patch Data for key indicators such as Population, GDP, etc.  published by WorldBank

## Demo Snapshots for the Application 
![alt text](https://github.com/harshit2996/worldbank-data-indicators/blob/master/demo1.png)
light mode

![alt text](https://github.com/harshit2996/worldbank-data-indicators/blob/master/demo2.png)
dark mode

![alt text](https://github.com/harshit2996/worldbank-data-indicators/blob/master/demo3.png)
data table

![alt text](https://github.com/harshit2996/worldbank-data-indicators/blob/master/demo4.png)
search filter

![alt text](https://github.com/harshit2996/worldbank-data-indicators/blob/master/demo5.png)
edit form

## Backend

### Requirements & Dependencies
- Django 
- mysqlclient package for django (if using MySQL) or use pymysql
- Django Rest Framework
- CORS Header Package for Django Rest Framework
- Downloaded Data (CSV files downloaded from the Wordbank website have been converted to JSON files using the csvToJson.py)

### Instructions for use
- Clone the Backend Repository
- Set up and configure the database
- Seed Data into the database 
- Start the Server using ```py manage.py runserver``` command

### API Endpoints
```
GET /display_data/ 

displays Indicator Name and its Corresponding Enpoint/Route which can be accessed by appending to /display_data/'indicator-endpoint'

Indicator Endpoints

GET, PATCH

/poputionData
/gdpData
/co2emissionData
/patentNonResData
/patentsResData
/exportsData
/lifeExpectancyData

```

## Frontend

### Requirements & Dependencies
NodeJS / npm should be installed

### Guide to Install and Run
-  Clone the Frontend Repository
-  Open terminal/cmd & Change Directory to the cloned repository and run ```npm install``` to install all the node_modules
- Run ```npm run serve``` to start the VueJS Application

### Note - Make Sure that Backend Runs on localhost:8000 and Frontend Runs on localhost:8080 (because this is the default configuration used for CORS and axios )

- You may choose the Type of Data to be viewed from the Top Toolbar or from the Indicators Table

- Select the Years from the Select Menu in the Table Toolbar
You may select multiple Years (because the data starts from the year 1960)

- You may edit/patch/update data in the table by selecting/ clicking a row and updating the data in the edit form which has opened.

- Changes will only be made on successful submission of request.

- You can only make changes to some of the fields as per the model declaration

- Search the results by any field

## Additional Feature -
- Day and Night Mode
- Snackbars for Error Messages
