# Deploy Django on Ubuntu server 18.04

**make sure apt-get repo is up to date, to do so use command**

```	
sudo apt-get update 
```

## Installing PIP3 and Jennie
- Install pip3 if does not exits.

```
sudo apt-get install python3-pip
```

- Install Jennie
```commandline
pip3 install https://s3.ap-south-1.amazonaws.com/cdn.jennie/ask_jennie-0.0.1-py3-none-any.whl
```

## Setting up LEMP
Full form LEMP is Linux Nginx MySQL and PHP. Its basically installing Nginx MySQL and PHP on server.

Nginx MySQL and PHP serves as dependencies for Web environment.

To Install use below command.
```
jennie ubuntu setup lemp
```

## Deploying Django
To deploy the django based application, go inside source folder where manage.py file is kept.

Before running the command make sure 

`python manage.py runserver 0.0.0.0:8081` 

is working properly

Run below command to deploy Django

```
jennie ubuntu deploy django
```