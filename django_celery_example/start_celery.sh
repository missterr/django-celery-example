#!/usr/bin/env bash

#!/bin/bash

PYTHON=/Users/missterr/projects/venv/bin/python
PID_FOLDER=/Users/missterr/projects/pid/
LOGS_FOLDER=/Users/missterr/projects/django_celery_example/log/
HOME=/Users/missterr/projects/django_celery_example/

celery -A django_celery_example worker -E --pidfile=${PID_FOLDER}celery_low.pid --logfile=${LOGS_FOLDER}celery_low.log --loglevel=DEBUG --hostname=low_dev_node@%h -Q low_development
celery -A django_celery_example worker -E --detach --pidfile=${PID_FOLDER}celery_high.pid --logfile=${LOGS_FOLDER}celery_high.log --loglevel=DEBUG --hostname=high_dev_node@%h -Q high_development
#celery -A core_server beat --detach --pidfile=${PID_FOLDER}celery_beat.pid --logfile=${LOGS_FOLDER}celery_beat.log --loglevel=DEBUG --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A core_server events -c app.Camera --detach --pidfile=${PID_FOLDER}celery_cam.pid --logfile=${LOGS_FOLDER}celerycam.log --frequency=10.0
# celerycam --frequency=10.0 --detach --pidfile=${PID_FOLDER}celery_cam.pid --logfile=${LOGS_FOLDER}celerycam.log