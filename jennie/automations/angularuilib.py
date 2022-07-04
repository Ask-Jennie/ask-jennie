from jennie.constants import *
from jennie.logger import LogginMixin
from jennie.jennietools.userinput import get_ask_app_name, get_basic_automation_conf
from jennie.rule_engine.angular_ui_lib_protocol import AngularUILibProtocol
from jennie.jennietools.checks import *

println = LogginMixin().print

class AngularUILib():
    def __init__(self, commands, user_info):
        self.args = commands
        self.STACK = "angular"
        self.TYPE = KEY_STACK_ANGULAR_UI_LIB
        self.token = user_info["token"]
        self.out = os.getcwd()
        if self.out[-1] != "/":
            self.out += "/"

    @property
    def execute(self):
        println("__init__: AngularUILib :", self.args[2], self.STACK, self.TYPE, self.token, self.out)
        if self.args[2] == "update":
            self.update()

        elif self.args[2] == "download":
            self.download()

        elif self.args[2] == "upload":
            self.upload()

        elif self.args[2] == "delete":
            self.delete()

        return True

    def download(self):

        self.app_name = None
        if len(self.args) > 3:
            self.app_name = self.args[3]
        println("Application", self.app_name, self.args)
        does_exits, self.app_name = get_ask_app_name(self.TYPE, self.app_name)

        if not does_exits:
            print("Library does not exits on server. Check list of libraries at\n\thttps://automations.ask-jennie.com")
            return False
        else:
            println("Application exits on server")
        AngularUILibProtocol(self.token).download(self.app_name, self.out)
        return True

    def upload(self):
        autoamtion_conf = check_angular_ui_module_directory(self.out)
        if autoamtion_conf:
            println("Upload Angular UI Lib module to jennie server")
            self.app_name = self.out.split("/")[-2]
            does_exits, self.app_name = get_ask_app_name(self.TYPE, self.app_name)

            if does_exits:
                print("An identical library is found on jennie server try changing library component name")
                return False

            self.app_config = get_basic_automation_conf(
                app_name=self.app_name,
                type=self.TYPE,
                stack=self.STACK
            )

            AngularUILibProtocol(self.token).upload(
                self.app_config, autoamtion_conf
            )
        else:
            print ("Directory is not an angular component, \nplease cd into your component directory before uploading..")
        return True

    def update(self):
        autoamtion_conf = check_angular_ui_module_directory(self.out)
        if autoamtion_conf:
            println("Upload Angular UI Lib module to jennie server")
            self.app_name = self.out.split("/")[-2]
            default = check_if_uploaded_automation(self.out)

            self.app_config = get_basic_automation_conf(
                app_name=self.app_name,
                type=self.TYPE,
                stack=self.STACK,
                default_inputs=default
            )

            if not self.app_config:
                print("Jennie configuration file 'jennie.conf.json' not found or corrupt")
                return False

            AngularUILibProtocol(self.token).update(
                self.app_config, autoamtion_conf
            )
        else:
            print("Directory is not an angular component, \nplease cd into your component directory before uploading..")

        return True

    def delete(self):
        self.app_name = None
        if len(self.args) > 3:
            self.app_name = self.args[3]

        println("Application", self.app_name, self.args)
        does_exits, self.app_name = get_ask_app_name(self.TYPE, self.app_name)

        println("Application name : check : name ", does_exits, self.app_name)
        if does_exits:
            AngularUILibProtocol(self.token).delete(self.app_name)
        else:
            print ("Unable to delete application as application is not found on server")
        return True
