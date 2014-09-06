#!/bin/bash
celery worker -l debug -P gevent -A datagravity.celery
