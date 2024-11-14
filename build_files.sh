#!/bin/bash

echo "Building projects package.."
python pip install -r requirements.txt

echo "migrating database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput
