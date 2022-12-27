###  Run Django project: 
~~~
python manage.py runserver
~~~
### Initialize project databse:
~~~
python manage.py migrate
~~~
### Create admin account 
~~~
python manage.py createsuperuser
~~~
### Create endpoint with view
~~~
python manage.py startapp home
~~~
### Create table in database
~~~
python manage.py makemigrations news
python manage.py sqlmigrate news 0001
python manage.py migrate
~~~



