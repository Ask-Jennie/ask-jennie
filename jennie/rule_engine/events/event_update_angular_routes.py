from jennie.jennietools.api_calls import APICalls
from jennie.constants import *

def UpdateAngularRoutes(filepath, routes, authgaurd_file=None):
    data = open(filepath).read()
    upper_content = data.split('@NgModule')[0]
    rest_content = '''@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }'''
    for route in routes:
        if "const routes: Routes = [];" in data:
            extra_content = ""
        else:
            extra_content = ","
        content_to_replace = extra_content + "\n" + "  " + route + "\n];"
        route_to_replace = "import { Routes, RouterModule } from '@angular/router';" + "\n" + routes[route]
        upper_content = upper_content.replace("];", content_to_replace)
        upper_content = upper_content.replace(
            "import { Routes, RouterModule } from '@angular/router';", route_to_replace
        )
    if authgaurd_file != None:
        authgaurd_content = "import { Routes, RouterModule } from '@angular/router';\n" + authgaurd_file
        upper_content = upper_content.replace("import { Routes, RouterModule } from '@angular/router';",
                                              authgaurd_content)
    data = upper_content + rest_content
    open(filepath, "w").write(data)

def execute_update_angular_routes(event, angular_routes_file_path="src/app/app-routing.module.ts"):
    routes = event[KEY_ROUTES]
    if KEY_AUTH_GAURD_FILE_LINK in event:
        authgaurd_file = APICalls().download_text_file(event[KEY_AUTH_GAURD_FILE_LINK])
    else:
        authgaurd_file = None
    UpdateAngularRoutes(angular_routes_file_path, routes, authgaurd_file)
    return True

def validate_update_angular_routes(event, app_name, type):
    if KEY_ROUTES not in event:
        print ("Missing routes in event information")
        return False

    if KEY_AUTH_GAURD_FILE_PATH in event:
        link = APICalls().upload_text_file(event[KEY_AUTH_GAURD_FILE_PATH], app_name, type)[KEY_FILE_LINK]
        event[KEY_AUTH_GAURD_FILE_LINK] = link
        del event[KEY_AUTH_GAURD_FILE_PATH]
    return event