<span style="color:orange;">LabelA Online Car Parts Store Backend System</span>
---------
**<span style="color:orange;">How to setup the project</span>**

**<span style="color:green;">Python Version = 3.9</span>**

**<span style="color:green;">Postgresql Version = ?????</span>**

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


**<span style="color:red;">Initial data for user, products, category and order models are automatically added when the migration for see as below home page</span>**

**Sample Demo For Home**
![Alt text](Home_Page.PNG?raw=true "Sample Demo")


**View All CRUD API Using Swagger**
- Navigate to ```http://localhost/swagger```

**Sample Demo For SwaggerUI**
![Alt text](swagger.png?raw=true "Sample Demo")



**PROJECT USE POSTGRESQL With Docker**

* USERNAME :- postgres
* PASSWORD :- root


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

	*By checking who logged in to the system and check whether above 'super_user' parameter True, in FE we can enable the CRUD for products. Then we can allow only admin to add/update/delete products*
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

	*User can add products to the cart using this POST method*

	```
 	curl -X POST "http://127.0.0.1:8000/api/order/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: lfiXexhNRupk1X2xPdV5o3jWed5MxZrbX9kwNEFA9UjSMrEi6cu9S5dSsyZbjs5b" -d "{  \"product_names\": \"test\",  \"total_products\": \"test\",  \"total_amount\": \"test\",  \"transaction_id\": \"test\",  \"order_confirm\": true,  \"user\": 1,  \"product\": 2}
	```

* Registered user can remove orders

	*User can remove products from cart using these DELETE method*
	```
	curl -X DELETE "http://127.0.0.1:8000/api/order/4/" -H  "accept: application/json" -H  "X-CSRFToken: lfiXexhNRupk1X2xPdV5o3jWed5MxZrbX9kwNEFA9UjSMrEi6cu9S5dSsyZbjs5b
	```

* Registered user can view all orders

	*User can see all the products in the cart using this GET method*
	```
	curl -X GET "http://127.0.0.1:8000/api/order/" -H  "accept: application/json" -H  "X-CSRFToken: lfiXexhNRupk1X2xPdV5o3jWed5MxZrbX9kwNEFA9UjSMrEi6cu9S5dSsyZbjs5b
	```

* Registered user can edit their orders details
	
	*User can confirm the order and add the delivery date by editing  the below order details using PATCH method*
	```
 	curl -X PATCH "http://127.0.0.1:8000/api/order/1/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: hJXWytFUbpjqOPvGJDiI8PwBTHsdJMWX76AtT9osFVW1TyYJWuoh4fOkntVNnffb" -d "{  \"product_names\": \"test\",  \"order_confirm\": true,  \"delivery_date_time\": \"2023-10-03T23:51:56.508Z\",  \"user\": 1,  \"product\": 1}
    ```
	![Alt text](Demo Images/edit_order.png?raw=true "Sample Demo")
	





