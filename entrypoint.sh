#!/bin/bash

docker-compose build
python manage.py makemigrations
python manage.py migrate
export PORT=80
export WORKERS=2

# Run the uWSGI command
uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module autocompany.wsgi:application
