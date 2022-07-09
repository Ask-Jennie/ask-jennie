import os
from jennie.jennietools.api_calls import APICalls
from jennie.constants import *
from jennie.rule_engine.events import execute_events
from jennie.rule_engine.events import validate_events
from jennie.logger import LogginMixin
from jennie.helper import write_json_file, read_json_file
from jennie.jennietools.userinput import get_basic_automation_conf

println = LogginMixin().print

class AngularAutomationProtocol():
    def __init__(self, token):
        self.token = token
        self.TYPE = KEY_STACK_ANGULAR_AUTOMATION

    def download(self, app_name):
        api_response = APICalls().download_automation_api_call(type=self.TYPE, app_name=app_name)
        println("API Response", api_response)
        if api_response["payload"] != False and "automation_conf" in api_response["payload"]:
            automation_conf = api_response["payload"]["automation_conf"]
            execute_events(automation_conf, self.TYPE)
            print("Automation Downloaded Successfully")
        else:
            print ("Unable to download Library from server")
            return False
        return True

    def upload(self, directory_path):
        jsonConf = read_json_file(directory_path + "/jennie.conf.json")
        println ("JSON Config\n", json.dumps(jsonConf, indent=2))
        if jsonConf == None:
            print ("Invalid Json Configuration, check jennie.conf.file is in proper json format")
            return False

        if "automation_conf" in jsonConf and is_arr(jsonConf["automation_conf"]):
            validated_events = validate_events(jsonConf["automation_conf"], self.TYPE, jsonConf["app_name"])
            if validated_events:
                jsonInfo = APICalls().upload_automation_api_call(self.TYPE, jsonConf)["payload"]
                println("Uploaded Config\n", json.dumps(jsonInfo, indent=2))
                write_json_file("jennie.conf.json", jsonInfo)
            else:
                print ("Invalid events found, check 'automation_conf' inside jennie.conf.json ")
                return False
        else:
            print("Corrupted automation_conf , check 'automation_conf' inside jennie.conf.json ")
        return True

    def update(self, directory_path):
        jsonConf = read_json_file(directory_path + "/jennie.conf.json")
        if jsonConf == None or "_id" not in jsonConf:
            print("Invalid Json Configuration, check jennie.conf.file is in proper json format")
            return False

        println("JSON configration found", jsonConf)
        config = get_basic_automation_conf(jsonConf["app_name"], jsonConf["type"], jsonConf["stack"], jsonConf)

        for key in config:
            jsonConf[key] = config[key]

        println("Updated JSON Conf = ", jsonConf)
        if "automation_conf" in jsonConf and is_arr(jsonConf["automation_conf"]):
            validated_events = validate_events(jsonConf["automation_conf"], self.TYPE, jsonConf["app_name"])
            if validated_events:
                jsonInfo = APICalls().update_automation_api_call(self.TYPE, jsonConf)["payload"]
                write_json_file("jennie.conf.json", jsonInfo)
                print("Automation Updated Successfully")
        else:
            print ("Corrupt jennie.conf.json, automation_conf must be a list of events")
        return True

    def delete(self, app_name):
        APICalls().delete_automation_api_call(self.TYPE, app_name)
        print("Automation Deleted Successfully")
        return True