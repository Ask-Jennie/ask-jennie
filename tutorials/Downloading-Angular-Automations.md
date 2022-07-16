# Downloading Angular Automation Module

Downloading an angular automation is quite simple, just go inside angular project and type below command

```bash
jennie angular automation download <module-name>
```

Jennie will download the automation from server and execute all the events that are supported in automation.

Each component listed in [automation.ask-jennie.com](https://automations.ask-jennie.com) comes with events info.

#### List of supported events

<table>
<tr>
    <th>
        Automation Name
    </th>
    <th>
        Automation Description
    </th>
    <th>
        Automation Sample
    </th>
</tr>
<tr>
<tr>
<td>adding-ng-library</td>
<td>A list of all the libraries that are present in "libs" is added to project using `ng add` command.</td>
<td><pre>
{
    "libs": [],
    "event_name" : "adding-ng-library"
}
</pre>
</td>
</tr>
<tr>
<td>angular-automations</td>
<td>Download a list of angular automations using `jennie angular automation automation-name`. </td>
<td><pre>
{
    "libs": [],
    "event_name" : "angular-automations"
}
</pre>
</td>
</tr>
<tr>
<td>angular-ui-lib</td>
<td>Download a list of angular ui modules using `jennie angular ui-lib module-name`. </td>
<td><pre>
{
    "libs": [],
    "event_name" : "angular-ui-lib"
}
</pre>
</td>
</tr>
<tr>
<td>copy-angular-component</td>
<td>Create copies of list of component inside components array. The component would contain each and every file inside folder.</td>
<td><pre>
{
       "components": [{
            "component_name": "",
            "component_files": [],
        }],
        "event_type": "copy-angular-component"
}
</pre>
</td>
</tr>
<tr>
<td>create-angular-component</td>
<td>Creates angular component inside project using `ng g c NAME_OF_COMPONENT` </td>
<td><pre>
{
    "component_name": "NAME_OF_COMPONENT",
    "event_name" : "create-angular-component"
}
</pre>
</td>
</tr>
<tr>
<td>create-angular-services</td>
<td>Creates angular service inside project using `ng g s NAME_OF_SERVICE` </td>
<td><pre>
{
    "service_name": "NAME_OF_SERVICE",
    "event_name" : "create-angular-services"
}
</pre>
</td>
</tr>
<tr>
<td>download-files</td>
<td>Download each file from `file_link` to location `out_path` inside from `files`.</td>
<td><pre>
{
    "files": [{
        file_link: file link from S3 that is required to be downloaded,
        out_path: Output Path where the files has to be uploaded
    }],
    "event_type": "download-files"
}
</pre>
</td>
</tr>
<tr>
<td>install-npm-library</td>
<td>Install all npm library from inside "libs" keyword to project.</td>
<td><pre>
{
    "libs": [],
    "event_name" : "install-npm-library"
}
</pre>
</td>
</tr>
<tr>
<td>update-angular-json</td>
<td>Update angular.json inside project to add styles and script to the project.</td>
<td><pre>
{
    "styles": [],
    "scripts": [],
    "event_name" : "update-angular-json"
}
</pre>
</td>
</tr>
<tr>
<td>update-angular-module</td>
<td>Update project with a list of providers and modules inside file app.module.ts. </td>
<td><pre>
{
    "providers": {
        "provider_name": "provider_import_location",
    },
    "modules": {
        "module_name": "module_import_location",
    },
    "event_name" : "update-angular-module"
}
</pre>
</td>
</tr>
<tr>
<td>update-angular-routes</td>
<td>Add routes to angular project.</td>
<td><pre>
{
    "routes": {
        "provider_name": "provider_import_location",
    },
    "event_name" : "update-angular-routes"
}
</pre>
</td>
</tr>
</table>

