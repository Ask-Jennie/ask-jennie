# Setting up PHPMYADMIN on Ubuntu 18.0.4

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

## Setting up PHPMYADMIN

phpmyadmin provides application interface for viewing and using database.

**Before installing phpmyadmin one must make sure nginx, php with mysql is up and running**

to do so use below command
```
jennie ubuntu setup lemp
```

Continue installing phpmyadmin
```
jennie ubuntu setup phpmyadmin
```