# Uploading Angular UI-Module

An author or the library can update their automation module info within the server anytime using update event type.

### Steps to update already upload library.

- Open terminal and navigate to automation module path. 
- Make sure jennie.conf.json is there in the directory, the file is generated once a component is uploaded.
- Upload Component to Server using jennie

```bash
jennie angular automations update
```

#### Output 

```bash
Do you want to update Title for Automation module?
>> Application title 

Do you want to update  Description for Automation module?
>> Application Description, max 200 chracter. 

Do you want to update  Tag (optional) for Automation module?
>> Category for Automation Module, Optional if not used Automation module will go into Others 
```

The software then update automation details with automation conf to the server.