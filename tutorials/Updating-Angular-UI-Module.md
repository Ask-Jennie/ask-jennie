# Uploading Angular UI-Module

An author or the library can update their ui module info within the server anytime using update event type.

### Steps to update already upload library.

- Open terminal and navigate to component i.e. `src/app/<component-name>`
- Make sure jennie.conf.json is there in the directory, the file is generated once a component is uploaded.
- Take a screenshot of component and keep it inside component page.
- Upload Component to Server using jennie

```bash
jennie angular ui-lib update
```

#### Output 

```bash
Do you want to update Title for UI module?
>> Application title 

Do you want to update  Description for UI module?
>> Application Description, max 200 chracter. 

Do you want to update  Tag (optional) for UI module?
>> Category for UI Module, Optional if not used UI module will go into Others 
```
 
If Image File is not found under component directory, option pops over asking for image file path

```bash
Input path for application image
>> /Users/jennie/Desktop/images.png
```

The software then update component files and information to the server.
Also, jennie.conf.json is updated in the directory.