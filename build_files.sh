#!/bin/bash

echo "Building projects package.."
echo "Ensuring pip is installed..."
python3.9 -m ensurepip --upgrade

# Verify that pip was installed
python3.9 -m pip --version || (echo "pip failed to install"; exit 1)

echo "Upgrading pip..."
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

echo "migrating database..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
