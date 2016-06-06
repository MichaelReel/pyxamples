# Django Tutorial

This requires that Django is installed. It can be installed via pip:

> pip install Django

## Notes

#### Test Coverage

For installing the coverage tool use:

> pip install coverage

To run and produce coverage html

> coverage run --source='polls' --branch manage.py test polls

> coverage html

#### Three-step guide to making model changes:

 1. Change your models (in models.py).
 1. Run `python manage.py makemigrations <app>` to create migrations for those changes.
 1. Run `python manage.py migrate` to apply those changes to the database.

#### To set up the developer database

> python manage.py migrate

#### To use the admin interface

Create a user who can login to the admin site

> python manage.py createsuperuser

Follow the steps to create a username and password.

Start the server (as usual)

> python manage.py runserver

Go to the login page using a browser

> http://127.0.0.1:8000/admin/

(or 8080 in debug)