# CHANHOUSE
## Set up CHANHOUSE development environment
### Install Python3, pip, virtualenv
Recommend using the latest version of Python 3
```console
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python3
sudo apt-get install -y python3-pip
pip3 install virtualenv #This convenient isolation prevents conflicting packages or software from interacting with each other.
```
### Install Django (within a virtualenv)
Create your virtual environment
```console
virtualenv chanhouse-env
```
Activate the virtual environment
```console
. active-env.sh
```
Within the environment, install the Django package using pip
```console
pip install Django==2.1.4
```
Checkout this release notes: https://docs.djangoproject.com/en/2.1/releases/2.1.4/
### Important note: source environment for every developing project
```console
. active-env.sh
```
## Start server
```console
python3 manage.py runserver 0.0.0.0:8000
```
- Open browser on your development server device
http://localhost:8000/
- On another device which is using the same network, you have to configure the file myhost.txt to access this server
http://{development-server-device}:8000/
