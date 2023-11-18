#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"yns@yns.yns"}

cd /app/

/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
