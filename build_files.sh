#!/bin/bash

echo "Building projects package.."
python3.9 pip install -r requirements.txt

echo "migrating database..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
