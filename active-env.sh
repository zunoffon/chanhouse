#!/bin/bash
project_env_name="chanhouse-env"
#source environment
echo "switching $project_env_name environment..."
. $project_env_name/bin/activate
#check python, framework
echo "checking for python..." `python -V` `echo "from"` `which python | xargs ls -l`
echo "checking for pip..." `pip -V`
echo "checking for django..." `django-admin --version` `echo "from"` `which django-admin | xargs ls -l`
