#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migrate  # Optional: Runs migrations on deploy (good for prod)