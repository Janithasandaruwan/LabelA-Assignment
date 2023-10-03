<span style="color:orange;">LabelA Online Car Parts Store Backend System</span>
---------
**<span style="color:orange;">How to setup the project</span>**

**<span style="color:green;">Python Version = 3.9</span>**

**<span style="color:green;">Postgresql Version = 3.9</span>**

First you have to clone the project

<https://github.com/Janithasandaruwan/LabelA-Assignment.git>

<span style="color:yellow;">How to setup the project using Docker + postgresql</span>
01. Open the docker desktop
02. Navigate to

	autocompany > settings.py > DATABASES default settings

	* comment the first two line and uncomment other settings

	* change the LIVE_URL = 'http://localhost' 
03. In the project directory, just type below command

	```docker-compose up -d```


<span style="color:yellow;">How to setup the project using sqlite3 db</span>

01. Navigate to

	autocompany > settings.py > DATABASES default settings

	* uncomment the first two line and comment other settings

	* change the LIVE_URL = 'http://127.0.0.1:8000'

02. Create a virtualenv
	
	```virtualenv env```
03. Activate the virtualenv

	* Windows OS:- env/Scripts/activate

	* Linux OS:- source env/bin/activate
04. Install all the requirements

	```pip install -r requirements.txt```
05. Migrate all the database changes

	```python manage.py migrate```
06. Run the server

	```python manage.py runserver```
07. Project will runs at,

	http://127.0.0.1:8000/
08. To view all API using Swagger

	http://127.0.0.1:8000/swagger/


**Backend API for online car parts sell web application which have CRUD for,**

    * products category
    * products
    * order
    * users


**Home page**
- Navigate to ```http://localhost/```


**<span style="color:red;">Initial data for products category and products are automatically added when the migration for see as below home page</span>**

**Sample Demo For Home**
![Alt text](homepage.PNG?raw=true "Sample Demo")


**View All CRUD API Using Swagger**
- Navigate to ```http://localhost/swagger```

**Sample Demo For SwaggerUI**
![Alt text](swagger.png?raw=true "Sample Demo")



**PROJECT USE POSTGRESQL With Docker**

* Super user name:- admin
* Super User password:- root

**Features**

* Super-user can ADD/UPDATE/DELETE products
* Registered user can view all products
* Registered user can view all a detail of a product
* Registered user can add orders
* Registered user can view all orders
* Registered user can edit their orders





