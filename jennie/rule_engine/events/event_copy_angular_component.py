import os

from jennie.constants import *
from jennie.jennietools.api_calls import APICalls
from jennie.helper import list_all_files_from_folder
from jennie.jennietools.checks import check_if_angular_project
from jennie.logger import LogginMixin

println = LogginMixin().print

def execute_copy_angular_component(event):
    """
    {
       "components": [{
            "component_name": "",
            "component_files": [],
        }],
        "event_type": "copy-angular-component"
    }
    :param event:
    :return:

    os.system("ng g c {}".format())
        for fileinfo in event["files"]:
            file_link, out_path = fileinfo[KEY_FILE_LINK], fileinfo[KEY_OUT_PATH]
            file_content = APICalls().download_text_file(file_link)
            open(out_path, "w").write(file_content)
    """
    if (not check_if_angular_project(os.getcwd())):
        print ("Not an angular project")
        return False
    else:
        for component in event["components"]:
            os.system("ng g c {}".format(component[KEY_COMPONENT_NAME]))
            for file in component["component_files"]:
                file_content = APICalls().download_text_file(file)
                filename = file.split("/")[-1]
                open("src/app/{}/{}".format(component[KEY_COMPONENT_NAME], filename), "w").write(file_content)
    return True

def validate_copy_angular_component(event, type, app_name):
    """
    {
        "component_names": [],
        "project_path": ""
    }
    :param event:
    :return:
    """
    if "project_path" not in event:
        print ("Missing component path")
        return False

    if "component_names" not in event:
        print ("Missing component names")
        return False
    else:
        conf = {
            "event_type": KEY_EVENT_COPY_COMPONENT,
            "components": []
        }
        for component in event["component_names"]:
            component_path = os.path.join(event["project_path"], "src/app/{}".format(component))
            files_list = list_all_files_from_folder(component_path)
            curent_component = {
                KEY_COMPONENT_NAME: component
            }
            curent_component["component_files"] = []
            for file in files_list:
                filepath = os.path.join(component_path, file)
                images_exenstions = ["png", "jpg", "jpeg"]
                if filepath.split(".")[-1] in images_exenstions:
                    file_link = APICalls().upload_image(filepath)["image_link"]
                else:
                    file_link = APICalls().upload_text_file(text_file_path=filepath, type=type, app_name=app_name)["file_link"]
                curent_component["component_files"].append(file_link)
            conf["components"].append(curent_component)
        println("Automation Conf", conf)
        return conf