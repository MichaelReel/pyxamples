# Django Tutorial

This requires that Django is installed. It can be installed via pip:

> pip install Django

## Notes

#### three-step guide to making model changes:

 1. Change your models (in models.py).
 1. Run `python manage.py makemigrations <app>` to create migrations for those changes.
 1. Run `python manage.py migrate` to apply those changes to the database.