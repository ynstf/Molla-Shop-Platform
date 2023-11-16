#!/bin/sh


python manage.py makemigration
python manage.py migrate
python manage.py collectstatic

#python manage.py creatsuperuser -email=