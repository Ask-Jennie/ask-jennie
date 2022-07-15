import os
from os.path import isfile, join
from jennie.constants import *
from jennie.helper import *
from jennie.logger import LogginMixin

println = LogginMixin().print

def check_angular_ui_module_directory(directory, return_component_file=False):
    """
    Check if directory contain files releated to angular ui module
    return back events for download files for UI module.
    :param directory: directory to search for
    :return: events for download files for UI module. or raise error.
    """
    if directory[-1] == "/":
        directory = directory[:-1]
    component_name = directory.split("/")[-1]
    files = [f for f in os.listdir(directory) if isfile(join(directory, f))]
    if component_name + ".component.ts" not in files:
        raise ValueError("Missing TS file for the component")
    elif component_name + ".component.css" not in files:
        raise ValueError("Missing CSS file for the component")
    elif component_name + ".component.html" not in files:
        raise ValueError("Missing CSS file for the component")

    if return_component_file:
        println ("Return Component File", component_name)
        return component_name + ".component.ts"
    image_file_path = None
    for file in files:
        if ".png" in file:
            image_file_path = directory + "/" + file


    event_info  = {
        "files": [
            {
                KEY_FILE_PATH:  component_name + ".component.ts",
                KEY_OUT_PATH: "src/app/ui-lib/{0}/{0}.component.ts".format(component_name)
            },
            {
                KEY_FILE_PATH: component_name + ".component.html",
                KEY_OUT_PATH: "src/app/ui-lib/{0}/{0}.component.html".format(component_name)
            },
            {
                KEY_FILE_PATH: component_name + ".component.css",
                KEY_OUT_PATH: "src/app/ui-lib/{0}/{0}.component.css".format(component_name)
            }
        ],
        "event_type": KEY_EVENT_DOWNLOAD_FILES,
        "app_image": image_file_path
    }

    return event_info

def check_if_angular_project(directory):
    """
    Check if directory is an angular project
    :param directory: directory path
    :return: Boolean
    """
    if directory[-1] != "/":
        directory += "/"
    search_files = [
        "angular.json", "karma.conf.js",
        "package.json"
    ]
    print("Checking Project Type Directory for ", directory)
    is_angular = True
    for file in search_files:
        if not os.path.isfile(directory + file):
            is_angular = False

    return is_angular

def check_if_uploaded_automation(directory):
    """
    Check if directory is an angular project
    :param directory: directory path
    :return: Boolean
    """
    if directory[-1] != "/":
        directory += "/"

    println("Checking Project Type Directory for ", directory)
    if not os.path.isfile(directory + "jennie.conf.json"):
        raise ValueError("Jennie configuration file does not exits")

    jsonConf = read_json_file(directory + "jennie.conf.json")
    if jsonConf == None:
        raise ValueError("Not a valid json.conf.json")

    if "_id" not in jsonConf:
        raise ValueError("Not a valid json.conf.json")
    return jsonConf
