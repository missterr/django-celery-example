#!/usr/bin/env bash

PYTHON=/Users/missterr/projects/venv/bin/python
PID_FOLDER=/Users/missterr/projects/pid/
LOGS_FOLDER=/Users/missterr/projects/log/
HOME=/Users/missterr/projects/django-celery-example/

celery -A django_celery_example worker -E --detach --pidfile=${PID_FOLDER}celery_low.pid --logfile=${LOGS_FOLDER}celery_low.log --loglevel=DEBUG --hostname=low_dev_node@%h -Q low_development -c 1
celery -A django_celery_example worker -E --detach --pidfile=${PID_FOLDER}celery_high.pid --logfile=${LOGS_FOLDER}celery_high.log --loglevel=DEBUG --hostname=high_dev_node@%h -Q high_development -c 1
celery -A django_celery_example beat --detach --pidfile=${PID_FOLDER}celery_beat.pid --logfile=${LOGS_FOLDER}celery_beat.log --loglevel=DEBUG --scheduler django_celery_beat.schedulers:DatabaseScheduler
