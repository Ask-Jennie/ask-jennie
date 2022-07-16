# Uploading-Angular-UI-Module.md

## Steps to upload

- Check if your component is working properly and is independent of other project component.
- If possible make @Input & @Output tags are properly used to make the component modular.
- Take a screenshot of component and keep it inside component page.
- Open terminal and navigate to component i.e. `src/app/<component-name>`
- Upload Component to Server using jennie

```bash
jennie angular ui-lib upload
```

#### Output 

```bash
Title for automation module
>> Application title 

Description for automation module
>> Application Description, max 200 chracter. 

Tag (optional) for automation module
>> Category for UI Module, Optional if not used UI module will go into Others 
```
 
If Image File is not found under component directory, option to enter image path is also shown.

```bash
Input path for application image
>> /Users/jennie/Desktop/images.png
```

The software then upload component files and create automation details which is further uploaded to server.
Also jennie.conf.json is created under the directory.

### jennie.conf.json

File store jennie configuration for specific automation.

```json
{
  "_id": 68,
  "created_by": {
    "email": "USER_EMAIl_ID",
    "fullname": "USER_NAME",
    "city": "USER CITY INFO",
    "bio": "USER BIO",
    "is_active": 1
  },
  "app_image": "https://s3.ap-south-1.amazonaws.com/cdn.jennie/images/1656993670-8699577.png",
  "app_name": "AppName",
  "app_title": "Application title ",
  "app_description": "Application Description, max 200 chracter.",
  "tag": "Category",
  "stack": "angular",
  "type": "angular-ui-lib",
  "automation_conf": [
    {
      "event_type": "create-component",
      "component_name": "ui-lib/sampleapp"
    },
    {
      "files": [
        {
          "out_path": "src/app/ui-lib/sampleapp/sampleapp.component.ts",
          "file_link": "https://s3.ap-south-1.amazonaws.com/cdn.jennie/angular/ui-lib/sampleapp/sampleapp.component.ts"
        },
        {
          "out_path": "src/app/ui-lib/sampleapp/sampleapp.component.html",
          "file_link": "https://s3.ap-south-1.amazonaws.com/cdn.jennie/angular/ui-lib/sampleapp/sampleapp.component.html"
        },
        {
          "out_path": "src/app/ui-lib/sampleapp/sampleapp.component.css",
          "file_link": "https://s3.ap-south-1.amazonaws.com/cdn.jennie/angular/ui-lib/sampleapp/sampleapp.component.css"
        }
      ],
      "event_type": "download-files"
    }
  ],
  "dependencies": [
    "bootstrap-5"
  ],
  "is_active": false,
  "created_on": "2022-07-05T04:01:11.143192Z",
  "updated_on": "2022-07-05T04:01:11.143232Z"
}
```

Uploaded Library can be found at automation.ask-jennie.com
 