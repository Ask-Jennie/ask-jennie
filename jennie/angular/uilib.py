from jennie.constants import KEY_ANGULAR_UI_LIB as MODULE_KEY
from jennie.constants import ANGULAR_UI_INFO_INPUT_KEYS, ANGULAR_UI_INFO_INPUT_2_KEYS
from jennie.jennie_tools.userinput import take_user_input
from jennie.jennie_tools.checks import *
from jennie.jennie_tools.api_calls import APICalls
from jennie.helperfnc import write_json_file
from jennie.jennie_tools.filehandler import FileHandler

def create_component(app_name):
    os.system("ng g c uigallery/{} --skip-tests=true".format(app_name))
    return True

class AngularUILibModule():
    def __init__(self, token):
        self.token = token
        self.api = APICalls()
        self.file_handler = FileHandler()


    def set_app_name(self, app_name):
        self.app_name = app_name

    def pre_upload_init(self, app_name=None):
        self.out = os.getcwd()
        if app_name == None:
            self.app_name = self.out.split("/")[-1]
            if self.app_name == "":
                self.app_name = self.out.split("/")[-2]
        else:
            self.app_name = app_name

    def add_module_from_download(self, library_info):
        create_component(self.app_name)
        files = {
            "ts_file_path": "src/app/uigallery/APP_NAME/APP_NAME.component.ts",
            "css_file_path": "src/app/uigallery/APP_NAME/APP_NAME.component.css",
            "html_file_path": "src/app/uigallery/APP_NAME/APP_NAME.component.html",
        }

        for file in files:
            link = library_info["automation_conf"][file]
            filepath = files[file].replace("APP_NAME", self.app_name)
            self.file_handler.replace_file_from_link(link, filepath)

        if "scripts" in library_info:
            for file in library_info["scripts"]:
                self.file_handler.replace_file_from_link(file, library_info["scripts"][file])
        return True

    def wrap_module_for_upload(self):

        # check if files inside UI module for angular is proper.
        self.files, all_files = check_angular_ui_module_files(self.out)
        if not self.files:
            return True

        image_file = None
        for file in all_files:
            if file.split(".")[-1] == "png":
                image_file = file

        # get other input like title, description, tag and image if not forlder.
        if image_file == None:
            json_resp = take_user_input(ANGULAR_UI_INFO_INPUT_KEYS)
        else:
            json_resp = take_user_input(ANGULAR_UI_INFO_INPUT_2_KEYS)
            json_resp["app_image"] = image_file

        # upload files and make final response.
        image_link = self.api.upload_image(json_resp["app_image"])
        json_resp["css_file_path"] = self.api.upload_text_file(self.files["CSS"], self.app_name, MODULE_KEY)["file_link"]
        json_resp["ts_file_path"] = self.api.upload_text_file(self.files["TS"], self.app_name, MODULE_KEY)["file_link"]
        json_resp["html_file_path"] = self.api.upload_text_file(self.files["HTML"], self.app_name, MODULE_KEY)["file_link"]

        final_resp_obj = {
          "scripts": "{}",
          "app_name": self.app_name,
          "stack": "angular",
          "app_image": image_link,
          "tag": json_resp["tag"],
          "app_description": json_resp["app_description"],
          "app_title": json_resp["app_title"],
          "type": "angular-ui-lib",
          "automation_conf": {
            "css_file_path": json_resp["css_file_path"],
            "html_file_path": json_resp["html_file_path"],
            "ts_file_path": json_resp["ts_file_path"]
          },
          "dependencies": "bootstrap"
        }
        return final_resp_obj

    @property
    def upload(self):
        # perform pre init and validate if library does exits on server or not.
        self.pre_upload_init()
        self.do_library_exits = self.api.automation_validate_api_call(MODULE_KEY, self.app_name)

        # Do nothing in case server is not up and running.
        if self.do_library_exits == None:
            return False

        # Show error in case library already exits.
        elif self.do_library_exits:
            print ("Library already exits")
            return False
        else:
            # Wrap angular module for upload
            request_json = self.wrap_module_for_upload()

            # Call Upload Automation API.
            response_json = self.api.add_automation_api_call(MODULE_KEY, request_json)

            # Save response to "jennie.conf.json"
            write_json_file("jennie.conf.json", response_json)
        return True

    @property
    def download(self):

        # perform pre init and get library information from server.
        if not check_if_angular_project(self.out):
            print ("The command must be used inside from angular project directory")
            return False

        self.pre_upload_init()

        # Download and validate library infor
        library_info = self.api.download_automation_api_call(MODULE_KEY, self.app_name)
        if not library_info:
            if library_info == None:
                return False
            print ("Library does not exits.")
            return False

        # Add UI library to project.
        self.add_module_from_download(library_info)
        return True

    @property
    def update(self):
        # perform pre init and validate if library does exits on server or not.
        self.pre_upload_init()
        self.do_library_exits = self.api.automation_validate_api_call(MODULE_KEY, self.app_name)

        # Do nothing in case server is not up and running.
        if self.do_library_exits == None:
            return False

        # Show error in case library does not exits for updation.
        if not self.do_library_exits:
            print("Library does not exits exits")
            return False


        # Wrap angular module for upload
        request_json = self.wrap_module_for_upload()

        # Call Upload Automation API.
        response_json = self.api.update_automation_api_call(MODULE_KEY, request_json)

        # Save response to "jennie.conf.json"
        write_json_file("jennie.conf.json", response_json)
        return True

    @property
    def delete(self):
        print("@TODO Delete Protocol")
        return True