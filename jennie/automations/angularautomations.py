from jennie.constants import *
from jennie.jennietools.userinput import get_ask_app_name, get_basic_automation_conf
from jennie.rule_engine.angular_automation_protocol import AngularAutomationProtocol
from jennie.logger import LogginMixin

println = LogginMixin().print

class AngularAutomations():
    def __init__(self, commands, user_info):
        self.args = commands
        self.STACK = "angular"
        self.token = user_info["token"]
        self.TYPE = KEY_STACK_ANGULAR_AUTOMATION
        self.out = os.getcwd()

    @property
    def execute(self):
        if self.args[2] == "update":
            self.update()

        elif self.args[2] == "build-conf":
            self.create_config()

        elif self.args[2] == "download":
            self.download()

        elif self.args[2] == "upload":
            self.upload()

        elif self.args[2] == "delete":
            self.delete()
        return True

    def create_config(self):
        does_app_exits, app_name = get_ask_app_name(self.TYPE)
        if does_app_exits:
            print ("Similar Library already exits")
            return False

        basic_automation_detail = get_basic_automation_conf(app_name, self.TYPE, self.STACK)
        create_automation_package(app_name, basic_automation_detail)
        return True

    def download(self):
        self.app_name = None
        if len(self.args) > 3:
            self.app_name = self.args[3]

        println("Download Angular Automations", self.app_name)
        does_exits, self.app_name = get_ask_app_name(self.TYPE, self.app_name)

        if not does_exits:
            print ("Application does not exits")
            return False

        println("Continue Download", self.app_name)
        AngularAutomationProtocol(self.token).download(self.app_name)
        return True

    def upload(self):
        AngularAutomationProtocol(self.token).upload(self.out)
        return True

    def update(self):
        AngularAutomationProtocol(self.token).update(self.out)
        return True

    def delete(self):
        does_app_exits, app_name = get_ask_app_name(self.TYPE)
        if not does_app_exits:
            print ("Application doe not exits")
            return False
        AngularAutomationProtocol(self.token).delete(app_name)
        return True
