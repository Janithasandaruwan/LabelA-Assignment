<span style="color:orange;">LabelA Online Car Parts Store Backend System</span>
---------
**<span style="color:orange;">How to setup the project</span>**

**<span style="color:green;">Python Version = 3.9</span>**

**<span style="color:green;">Postgresql Version = 3.9</span>**

First you have to clone the project

<https://github.com/Janithasandaruwan/LabelA-Assignment.git>

<span style="color:yellow;">How to setup the project using Docker + postgresql</span>
01. In the project directory, just type below command

	```docker-compose up -d```
02. Project will runs at,

	http://localhost/
03. To view all API using Swagger

	http://localhost/swagger/


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
![Alt text](Demo Images/homepage.PNG?raw=true "Sample Demo")


**View All CRUD API Using Swagger**
- Navigate to ```http://localhost/swagger```

**Sample Demo For SwaggerUI**
![Alt text](Demo Images/swagger.png?raw=true "Sample Demo")



**PROJECT USE POSTGRESQL With Docker**

* Super user name:- admin
* Super User password:- root


<span style="color:orange;">User Stories</span>
---------
* User registration to the system

	*We can use this POST method to register a user. Here I used 'is_superuser' filed,*

  		* Register a super-user > is_superuser = True (admin user credentials needed as my architecture)

  		* Register a client > is_superuser = False 
	
	```
 	curl -X POST "http://127.0.0.1:8000/api/user/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: ahs5lXoreRQaqg9Aq3lmbtvBCyXke0ZyHvmzpZ3dFUEncgfkDohr72TaGGmQI89Y" -d "{  \"name\": \"client1\",  \"email\": \"client1@example.com\",  \"password\": \"12345678\",  \"phone\": \"+941111111\",  \"gender\": \"male\",  \"is_active\": true,  \"is_staff\": true,  \"is_superuser\": false}
    ```
 	![Alt text](Demo Images/register_user.png?raw=true "Sample Demo")


* Super-user can ADD/UPDATE/DELETE products

	*By checking who logged in to the system and check whether above 'super_user' parameter True, in FE we can enable the CRUD of products*
	![Alt text](Demo Images/product.png?raw=true "Sample Demo")

* Every user who navigate to the web app can view all products

	*We can execute this GET all curl when the home page loading*
	```
	curl -X GET "http://127.0.0.1:8000/api/product/" -H  "accept: application/json" -H  "X-CSRFToken: UIOj2ldw8V1IZFqjoa93WeD9p8dbx3TyrWIN6nSizYPVLFw3Bv58SN1ItgCH1b3Y
 	```
 	![Alt text](Demo Images/get_all_products.png?raw=true "Sample Demo")

* Every user who navigate to the web app can view detail of a product

	*We can execute this GET by id when user click specific product to show all details, here product id=3*
	```
	curl -X GET "http://127.0.0.1:8000/api/product/3/" -H  "accept: application/json" -H  "X-CSRFToken: UIOj2ldw8V1IZFqjoa93WeD9p8dbx3TyrWIN6nSizYPVLFw3Bv58SN1ItgCH1b3Y
    ```
 	![Alt text](Demo Images/get_detail_of_product.png?raw=true "Sample Demo")


* Registered user can add orders
* Registered user can view all orders
* Registered user can edit their orders





