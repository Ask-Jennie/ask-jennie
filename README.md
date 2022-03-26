# Jennie
The package targets protocol for uploading and reusing task and libraries for product development and deployment.
The package comes with Protocol ( Angular and Django ) + Custom automation.

# Using the software
The software package can be used only after log in. 

![software](images/ezgif.com-gif-maker (4).gif)

# Version Check
Check software version using command `jennie version`

**output (if logged in)**
```
Version : A.B.C
Author : ASK Jennie Developer <saurabh@ask-jennie.com>
Stable Version : X.Y.Z
Latest Version : XX.YY.ZZ
The package targets protocol for uploading and reusing task and libraries

User Name : Saurabh Pandey
User Email : saurabh@ask-jennie.com
```

**output (if not logged in)**
```
Version : 0.0.1
Author : ASK Jennie Developer <saurabh@ask-jennie.com>
The package targets protocol for uploading and reusing task and libraries

Not logged in, To use the software try login using jennie setup [registered_email]

```

# CheatSheet

Command | Type | About 
--- | --- | ---
`jennie version` | **Setup** | Shows the software version, user information and software stable version no. 
`jennie setup` | **Setup** | Log in inside ASK Jennie Package, Automations start working only if user has logged in  
`jennie logout` | **Setup** | Logout from ASK Jennie
`jennie ubuntu setup lemp` | **Automation** | Install LEMP (nginx, php, mysql) on ubuntu server/desktop
`jennie ubuntu setup phpmyadmin` | **Automation** | Install phpmyadmin on ubuntu server/desktop
`jennie ubuntu setup elasticsearch` | **Automation** | Install elasticsearch DB on ubuntu server/desktop
`jennie ubuntu setup elk` | **Automation** | Install ELK (elastic, logstash, kibana) on ubuntu server/desktop
`jennie ubuntu deploy django` | **Automation** | Deploy Django Project
`jennie ubuntu deploy web` | **Automation** | Deploy HTML Project ( normal html or angular build files )



__version__ = "0.0.1"

__description__ = 'The package targets protocol for uploading and reusing task and libraries'

__author__ = 'ASK Jennie Developer <saurabh@ask-jennie.com>'
