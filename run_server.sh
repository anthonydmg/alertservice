#!/usr/bin/env bash
cd /home/pi/Documentos/Anthony/alertservice/
set -e
source "./venv/bin/activate"
#gunicorn --bind 0.0.0.0:5055 --worker-class eventlet -w 1 wsgi:app
gunicorn --bind 0.0.0.0:5055 --worker-class eventlet -w 1 wsgi:app -D
#python index.py  &
#python -u index.py
