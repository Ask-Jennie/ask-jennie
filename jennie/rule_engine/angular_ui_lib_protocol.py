import json

from jennie.jennietools.api_calls import APICalls
from jennie.jennietools.checks import check_angular_ui_module_directory, check_if_angular_project
from jennie.jennietools.userinput import get_app_image
from jennie.rule_engine.events.event_download_files import validate_download_files
from jennie.rule_engine.events.manager import execute_events
from jennie.logger import LogginMixin
from jennie.helper import *
from jennie.constants import *

println = LogginMixin().print

class AngularUILibProtocol():
    def __init__(self, token):
        self.token = token

    def upload(self, app_config, automation_conf):
        """
        Creates complete application conf with automation conf.
        once complete application conf is created validate with rule engine.
        and upload it to jennie server
        :param app_config: Configuration for the application,
        includes app_name, app_title, app_tag etc.
        :param directory_path: Component Directory Path
        :return: app_config
        """
        println("\nAutomation conf created", automation_conf)
        app_config["app_image"] = automation_conf["app_image"]
        del automation_conf["app_image"]

        if app_config["app_image"] == None:
            app_config["app_image"] = get_app_image()

        event_info_download_files = validate_download_files(
            automation_conf, app_name=app_config["app_name"],
            type=app_config["type"]
        )
        app_config["app_image"] = APICalls().upload_image(app_config["app_image"])["image_link"]
        println("\nEvents verified and image uploaded")

        event_create_component = {
            "event_type": KEY_EVENT_CREATE_COMPONENT,
            "component_name": "ui-lib/" + app_config["app_name"]
        }

        app_config["automation_conf"] = [ event_create_component, event_info_download_files ]

        println("\n\nFinal Application Config Created")
        println(json.dumps(app_config, indent=2), "\n\n")

        response = APICalls().upload_automation_api_call(type=app_config["type"], json_conf=app_config)
        if response != None:
            write_json_file("jennie.conf.json", response["payload"])
            print ("Angular UI Lib Successfully uploaded")
            return True

        else:
            print ("Some Error while uploading Angular UI, please try again later")
            return False

    def update(self, app_config, automation_conf):
        println("\nAutomation conf created", automation_conf)
        println("\nApp Config", app_config)
        app_config["app_image"] = automation_conf["app_image"]
        del automation_conf["app_image"]

        if app_config["app_image"] == None:
            app_config["app_image"] = get_app_image()

        event_info_download_files = validate_download_files(
            automation_conf, app_name=app_config["app_name"],
            type=app_config["type"]
        )
        app_config["app_image"] = APICalls().upload_image(app_config["app_image"])["image_link"]
        println("\nEvents verified and image uploaded")

        event_create_component = {
            "event_type": KEY_EVENT_CREATE_COMPONENT,
            "component_name": "ui-lib/" + app_config["app_name"]
        }

        app_config["automation_conf"] = [ event_create_component, event_info_download_files ]

        println("\n\nFinal Application Config Created")
        println(json.dumps(app_config, indent=2), "\n\n")

        response = APICalls().update_automation_api_call(type=app_config["type"], json_conf=app_config)
        if response != None:
            write_json_file("jennie.conf.json", response["payload"])
            print ("Angular UI Lib Successfully updated")
            return True

        else:
            print ("Some Error while uploading Angular UI, please try again later")
            return False

    def download(self, app_name, directory_path):
        is_valid_project = check_if_angular_project(directory_path)
        if not is_valid_project:
            print ("Not a valid Angular project, make sure you are inside angular project where angular.json file is kept")
            return False
        println ("Download app name", app_name)
        response = APICalls().download_automation_api_call(type=KEY_STACK_ANGULAR_UI_LIB, app_name=app_name)
        if response["payload"]:
            automation_conf = response["payload"]["automation_conf"]
            execute_events(automation_conf, KEY_STACK_ANGULAR_UI_LIB)
        else:
            print ("Unable to get application from server, \n" +
                   "report it to admin dextrop@ask-jennie.com with application name as \n\t" +
                   "{}".format(app_name) +
                   "error as \n\n\t{}".format(app_name))
        return True

    def delete(self, app_name):
        response = APICalls().delete_automation_api_call(KEY_STACK_ANGULAR_UI_LIB, app_name)
        if not response:
            print ("Unable to delete library")
        else:
            print("Application Delete from jennie server successfully")
        return True