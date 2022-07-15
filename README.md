# Introduction
Jennie as a software package aims to provide platform based protocols through which any developers will be able to store and reuse development related tasks.

The software follows the below structure.

`jennie <stack> <type> <event>`


### Where:

**Stacks** : Stacks are platforms for which protocol aims to run. Currently we have build automation for platforms Angular, Django, Python

**Type** : Each stack may have two types of protocol

- ui-lib : UI Component is made reusable.
- automations : Automation events can be made reusable

**Event** : There are 5 events supported for each protocol.
    
- Upload
- Download
- Update
- Delete
- Build-conf (optional)

#### Eg Commands for Platform Angular and Type UI Lib

- `jennie angular ui-lib upload`

- `jennie angular ui-lib download`




# Installation
The software can be using pip3 package manager

```commandline
pip3 install https://s3.ap-south-1.amazonaws.com/cdn.jennie/ask_jennie-0.0.2-py3-none-any.whl
```

The software package can be used only after log in. 

To login use 
```
jennie setup <email-address>
```

### Check the demo below

![software check](https://raw.githubusercontent.com/Ask-Jennie/ask-jennie/master/images/ezgif.com-gif-maker%20(4).gif)

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
