#!/bin/bash

echo "Building projects package.."
python3.10 pip install -r requirements.txt

echo "migrating database..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput
