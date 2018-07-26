#!/usr/bin/env bash

PYTHON=/Users/missterr/projects/venv/bin/python
PID_FOLDER=../../pid/

$PYTHON -m celery multi stopwait worker1 --pidfile=${PID_FOLDER}celery_high.pid
$PYTHON -m celery multi stopwait worker1 --pidfile=${PID_FOLDER}celery_low.pid
$PYTHON -m celery multi stopwait worker1 --pidfile=${PID_FOLDER}celery_beat.pid