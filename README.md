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
### Install the database software (PostgreSQL)
- For Linux - Install the database software
```console
sudo apt-get install postgresql postgresql-contrib 
``` 
- Create a Database and Database User 
```console 
sudo su - postgres psql 
``` 
- Create a database for chanhouse project 
```console 
CREATE DATABASE chanhouse_db; 
``` 
- Create a database user to connect and interact with chanhouse_db 
```console 
CREATE USER chanhouse_db_user WITH PASSWORD 'chanhouse_db_password'; 
``` 
- Give our database user access rights to the database we created
```console
GRANT ALL PRIVILEGES ON DATABASE chanhouse_db TO chanhouse_db_user;
```
- Exit the SQL prompt to get back to the postgres user's shell session
```console
\q
```
- Exit out of the postgres user's shell session to get back to your regular user's shell session
```console
exit
```
- For Windows - Install software
    https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    Install Tut: http://www.postgresqltutorial.com/install-postgresql/
    Access PSQL - Create database and user the same with linux and macos 
    
- For Mac OS - Install the database software
```console
brew install postgresql
```
- Create a Database and Database User
```console
psql postgres
```
- Create a database for chanhouse project
```console
CREATE DATABASE chanhouse_db;
```
- Create a database user to connect and interact with chanhouse_db
```console
CREATE USER chanhouse_db_user WITH PASSWORD 'chanhouse_db_password';
```
- Give our database user access rights to the database we created
```console
GRANT ALL PRIVILEGES ON DATABASE chanhouse_db TO chanhouse_db_user;
```
- Exit the SQL prompt to get back to the postgres user's shell session
```console
\q
```
- Exit out of the postgres user's shell session to get back to your regular user's shell session
```console
exit
```

### Install packages using in virtual environment (Django framework, psycopg2)
Create your virtual environment
```console
virtualenv chanhouse-env
```
Activate the virtual environment
```console
. active-env.sh
```
### Install package for project
```console
pip install -r requirements-dev.txt
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
