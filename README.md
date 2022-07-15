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