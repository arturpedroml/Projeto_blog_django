#!/bin/sh
echo 'Executando makemigrations.sh'
makemigrations.sh
echo 'Executando migrate'
python manage.py migrate --noinput