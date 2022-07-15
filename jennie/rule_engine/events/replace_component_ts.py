import os
from jennie.jennietools.api_calls import APICalls
from jennie.constants import *
from jennie.logger import LogginMixin
from jennie.jennietools.checks import check_angular_ui_module_directory

println = LogginMixin().print
def execute_replace_component_ts(event):
    """
    {
        "event_type": "replace-component-ts",
        "file_link": ""
    }
    :param event:
    :return:
    """

    file_link = event[KEY_FILE_LINK]
    println("Downloading file from file_link", file_link)
    file_content = APICalls().download_text_file(file_link)
    curr_dir = os.getcwd()
    component_file = check_angular_ui_module_directory(curr_dir, return_component_file=True)
    println("Current Link ", component_file)
    content_component_file = open(component_file).read()
    println("content_component_file ", content_component_file)
    println("content_component_file ", file_content)
    component_name = content_component_file.split("export class ")[1].split(" implements OnInit {")[0]
    component_conf = "@Component" + content_component_file.split("@Component")[1].split("})")[0] + "})"
    file_content = file_content.replace("SampleComponent", component_name)
    file_content = file_content.replace("APPLICATION_CONFIG", component_conf)
    open(component_file, "w").write(file_content)
    return True

def validate_replace_component_ts(event, app_name, type):
    if KEY_FILE_PATH in event:
        event[KEY_FILE_LINK] = APICalls().upload_text_file(
            event[KEY_FILE_PATH],
            app_name=app_name,
            type=type
        )[KEY_FILE_LINK]
        del event[KEY_FILE_PATH]
    return event