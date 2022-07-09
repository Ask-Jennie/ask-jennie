from jennie.constants import *
from jennie.logger import LogginMixin

println = LogginMixin().print

class UpdateAngularModuleFile():
    def __init__(self, filepath):
        self.filepath = filepath
        self.content = open(filepath).read()

    def add_imports(self, imports):
        for modulename in imports:
            self.content = self.content.replace("BrowserModule,", "BrowserModule," + "\n" + "    " + modulename + ",")
            self.content = self.content.replace("import { BrowserModule } from '@angular/platform-browser';", "import { BrowserModule } from '@angular/platform-browser';" + "\n" + imports[modulename])
        self.content = self.content.replace(",],", "],")
        open(self.filepath, "w").write(self.content)
        return True

    def add_providers(self, providers):
        for providername in providers:
            self.content = self.content.replace("providers: [", "providers: [" + "\n" + "    " + providername + ",")
            self.content = self.content.replace("import { BrowserModule } from '@angular/platform-browser';", "import { BrowserModule } from '@angular/platform-browser';" + "\n" + providers[providername])
        self.content = self.content.replace(",],", "],")
        open(self.filepath, "w").write(self.content)
        return True

def execute_update_angular_module(event, angular_module_file_path="src/app/app.module.ts"):
    println("Updating angular module", angular_module_file_path)
    if KEY_IMPORTS in event:
        println("Updating angular module with imports", event[KEY_IMPORTS])
        UpdateAngularModuleFile(angular_module_file_path).add_imports(event[KEY_IMPORTS])
    if KEY_PROVIDERS in event:
        println("Updating angular module with providers", event[KEY_PROVIDERS])
        UpdateAngularModuleFile(angular_module_file_path).add_providers(event[KEY_PROVIDERS])
    return True

def validate_update_angular_module(event):
    if not KEY_IMPORTS in event and not KEY_PROVIDERS in event:
        print ("Neither Imports not providers present")
        return False
    return True