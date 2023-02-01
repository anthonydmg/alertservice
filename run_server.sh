#!/usr/bin/env bash
cd /home/pi/Documentos/Anthony/alertservice/
set -e
source "./venv/bin/activate"
python index.py  &
#python -u index.py
