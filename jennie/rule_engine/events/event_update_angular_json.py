"""
event_name : update-angular-json

config format:
{
    "styles": [],
    "scripts": [],
    "event_name" : update-angular-json
}
"""
import json, os
from jennie.logger import LogginMixin

println = LogginMixin().print
def execute_update_angular_json(angular_json_filepath, event):
    """
    Append for script / style to angular.json.
    :param angular_json_filepath: angular.json
    :param event_info: {
        "styles": [],
        "scripts": [],
        "event_name" : update-angular-json
    }
    :return:
    """

    controller = UpdateAngularJSONFile(
        angular_json_filepath
    )



    if KEY_STYLES in event:
        status = controller.add_styles(event[KEY_STYLES])
        if not status:
            print("unable to update styles, check if angular.json is not corrupt")
            return status

    if KEY_SCRIPTS in event:
        status = controller.add_scripts(event[KEY_SCRIPTS])
        if not status:
            print("unable to update scripts, check if angular.json is not corrupt")
            return status

    return True

def validate_update_angular_json(event):
    """
    Checks for script / style in event info
    :param event_info: {
        "styles": [],
        "scripts": [],
        "event_name" : update-angular-json
    }
    :return:
    """
    if not KEY_STYLES in event and not KEY_SCRIPTS in event:
        print("Event does not have any styles or scripts")
        return False
    return True


KEY_STYLES = "styles"
KEY_SCRIPTS = "scripts"

class UpdateAngularJSONFile():
    def __init__(self, filepath):

        self.filepath = filepath
        self.content = json.loads(open(filepath).read())
        self.project_name = str(os.getcwd()).split("/")[-1]
        println(filepath, self.project_name)

    def add_styles(self, styles_to_add):
        '''
        Add list of *.css to angular project styles.
        :param styles_to_add: list of styles to add
        :return: content
        '''
        println("Styles to add", styles_to_add)
        styles = self.content["projects"][self.project_name]["architect"]["build"]["options"]["styles"]
        counter = 0
        for path in styles_to_add:
            if path not in styles:
                styles.insert(counter, path)
            counter += 1
        self.content["projects"][self.project_name]["architect"]["build"]["options"]["styles"] = styles

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.content, f, ensure_ascii=False, indent=4)

        return True

    def add_scripts(self, scripts_to_add):
        '''
        Add list of *.js to angular project scripts.
        :param scripts_to_add: list of script file to add.
        :return: content
        '''
        println("Scripts to add", scripts_to_add)
        scripts = self.content["projects"][self.project_name]["architect"]["build"]["options"]["scripts"]
        counter = 0
        for path in scripts_to_add:
            if path not in scripts:
                scripts.insert(counter, path)
            counter += 1
        self.content["projects"][self.project_name]["architect"]["build"]["options"]["scripts"] = scripts
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.content, f, ensure_ascii=False, indent=4)

        return True

