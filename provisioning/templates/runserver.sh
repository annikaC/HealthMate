#!/bin/bash

source {{ project_bin }}/activate
cd {{ project_src }}
exec gunicorn {{ django_project_name }}.wsgi:application -b {{ appserver_hostport }}
