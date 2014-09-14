#!/bin/bash
celery worker -l info -P gevent -A datagravity.celery
