# Uploading Angular Automation Module

With jennie one could create their own automation which and push it to server. 
To do so follow the below step.

- **Create Jennie Automation**: Create automation conf using `jennie angular automations build-conf`. 
Once automation is created one could see a folder is create with jennie.conf.json file in it.  

- **Add Automation Events**: Add automation events to `jennie.conf.json`. A list of events supported are listed below.

- **Upload to server**: Once all set, go inside the automation folder and user below command to upload module.

```bash
jennie angular automation upload
```

Jennie will process and verify automation conf and will update the automation to jennie server. 
Once automation is uploaded user can find their automation at 
[automation.ask-jennie.com](https://automations.ask-jennie.com)

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
<td>Add a list of libraries names inside lib key that requires to be installed when automation event is executed.</td>
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
<td>Add a list of angular automation names inside lib key that requires to be installed using when automation event is executed.</td>
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
<td>Add a list of angular ui modules names inside lib key that requires to be installed using when automation event is executed.</td>
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
<td>Upload All component files to server. The component must be kept at location src/app</td>
<td><pre>
{
    "component_names": [],
    "project_path": ""
}
</pre>
</td>
</tr>
<tr>
<td>create-angular-component</td>
<td>Add the name of component that will be created when the automation event is executed</td>
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
<td>Add the name of service that will be created when the automation event is executed</td>
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
<td>Upload list of files provided inside `files` to server. these files will later be downloaded when event is executed.</td>
<td><pre>
{
    "files": [{
        file_path: file link from S3 that is required to be downloaded,
        out_path: Output Path where the files has to be uploaded
    }],
    "event_type": "download-files"
}
</pre>
</td>
</tr>
<tr>
<td>install-npm-library</td>
<td>Add a list of npm libraries names inside lib key that requires to be installed using when automation event is executed.</td>
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
<td>Add list of path in scripts and styles that need to be added in project when executed.</td>
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
<td>Add list of info in providers and modules that need to be added in project module when executed.</td>
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
<td>Add list of routes info that get added in project module when executed.</td>
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

