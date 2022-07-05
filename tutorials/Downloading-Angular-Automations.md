# Protocol : Downloading Angular Automations
Angular automation protocol can be used in upload, download, update and delete. In this section we will learn how Downloading Angular Automations works. 

## Protocol Command

```
jennie angular automations download <module-name>
```

## What happens?
- Automation configuration is downloaded from jennie server.
- For each supported event execute event based on event information. 

# Supported Automation Events:

| sr. | event name | stacks supported  | event description  |
| :-: | :---:   | :-: | :-: |
| 1. | angular-automations | angular-automations | install angular automations, a list of automations can be executed from this event |
| 2. | angular-ui-lib | angular-automations, angular-ui-lib | install angular ui libraries, a list of libraries can be added to project from this event |
| 3. | create-angular-component | angular-automations | Creates angular component, execute angular command "ng g c <component-name>" |
| 4. | create-angular-services | angular-automations | Creates angular services, execute angular command "ng g s <component-name>" |
| 5. | create-python-package | django-automations, python-automations | Update Django urls.py file |
| 6. | custom-automations | ALL | runs custom automation as an event. Custom automation are provided by jennie server. |
| 7. | download-files | ALL | Download and place file content inside project. Copy & Paste Event |
| 8. | install-npm-library | angular-automations | Install a list of npm libraries provided. |
| 9. | update-angular-json | angular-automations | Update angular.json file |
| 10. | update-angular-routes | angular-automations | Update angular routes |
| 11. | update-angular-modules | angular-automations | Update angular modules files with list of modules and providers |
