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
<td>adding-ng-library</td>
<td>A list of all the libraries that are present in "libs" is added to project using `ng add` command.</td>
<td><pre>
{
    "libs": [],
    "event_name" : "adding-ng-library"
}
</pre></td>
</tr>
</table>

