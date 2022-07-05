# Protocol : Downloading Angular UI Module
Angular automation protocol can be used in upload, download, update and delete. In this section we will learn how Downloading Angular Automations works. 

## Protocol Command
```
jennie angular ui-lib download <module-name>
```

## What happens?
- Automation configuration is downloaded from jennie server.
- Create component and download component files. 

## Standard Protocol Config
```json
[
{
  "event_type": "create-component",
  "component_name": "<app-name>"

},
{
  "event_type": "download-files",
  "files": [
    {
      "out_path": "OUTPUT_PATH_FOR_COMPONENT_CSS",
      "file_link": "LINK_FOR_COMPONENT_CSS"
    },
    {
      "out_path": "OUTPUT_PATH_FOR_COMPONENT_TS",
      "file_link": "LINK_FOR_COMPONENT_TS"
    },
    {
      "out_path": "OUTPUT_PATH_FOR_COMPONENT_HTML",
      "file_link": "LINK_FOR_COMPONENT_HTML"
    },
    {
      "out_path": "OUTPUT_PATH_FOR_ASSETS_JS",
      "file_link": "LINK_FOR_SCRIPT"
    }
  ]

}
]

```
# Supported Automation Events:

| sr. | event name | stacks supported  | event description  |
| :-: | :---:   | :-: | :-: |
| 1. | create-angular-component | angular-automations | Creates angular component, execute angular command "ng g c <component-name>" |
| 2. | download-files | ALL | Download and place file content inside project. Copy & Paste Event |
