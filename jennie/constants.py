import os, json

KEY_STACK_ANGULAR_AUTOMATION = "angular-automations"
KEY_STACK_ANGULAR_UI_LIB = "angular-ui-lib"
KEY_STACK_DJANGO_AUTOMATIONS = "django-automations"


KEY_EVENT_DOWNLOAD_FILES = "download-files"
KEY_EVENT_CREATE_COMPONENT = "create-component"
KEY_EVENT_ANGULAR_UI_LIB = "angular-ui-lib"
KEY_EVENT_ANGULAR_AUTOMATIONS = "angular-automations"
KEY_EVENT_ANGULAR_SERVICES = "create-services"
KEY_EVENT_INSTALL_NPM_LIBRARY = "install-npm-library"
KEY_EVENT_UPDATE_ANGULAR_JSON = "update-angular-json"
KEY_EVENT_UPDATE_ANGULAR_MODULE = "update-angular-module"
KEY_EVENT_UPDATE_ANGULAR_ROUTES = "update-angular-routes"

KEY_EVENT_TYPE = "event_type"
KEY_LIBS = "libs"
KEY_ROUTES = "routes"
KEY_TYPE = "type"
KEY_IMPORTS = "imports"
KEY_PROVIDERS = "providers"
KEY_MODULES = "modules"
KEY_TOKEN = "token"
KEY_PAYLOAD = "payload"
KEY_FILE_LINK = "file_link"
KEY_OUT_PATH = "out_path"
KEY_SCRIPT_NAME = "script_name"
KEY_FILE_PATH = "file_path"
KEY_STYLES = "styles"
KEY_SCRIPTS = "scripts"
KEY_AUTH_GAURD_FILE_LINK = "auth_gaurd_file_link"
KEY_AUTH_GAURD_FILE_PATH = "auth_gaurd_file"


AUTOMATION_COMMANDS = {
    "angular": {
        "ui-lib": {
            "download": "library_name",
            "upload": None,
            "update": None,
            "delete": "library_name"
        },
        "automations": {
            "build-conf": None,
            "download": "library_name",
            "upload": None,
            "update": None,
            "delete": "library_name"
        }
    },
    "ubuntu": {
        "setup":  {
            "lemp": None,
            "phpmyadmin": None,
            "elk": None,
            "elasticsearch": None
        },
        "deploy": {
            "django": None,
            "web": None
        }
    },
    "logout": "",
    "version": ""
}

USER_INPUT_FOR_SETUP = {
    "email": "Kindly enter email address registered with ASK jennie, \nDon't have account go to https://ask-jennie.com/register"
}

AUTOMATION_BASIC_INPUT = {
    "app_title": "Title for automation module", "app_description": "Description for automation module",
    "tag": "Tag (optional) for automation module",
}

TYE_STR = "<class 'str'>"
TYE_LIST = "<class 'list'>"
TYE_DICT = "<class 'dict'>"

home = os.path.expanduser("~")
if home[-1] != "/":
    home += "/"
TOKEN_PATH = home + ".jennie.conf.json"

def get_user_access_token():
    if not os.path.isfile(TOKEN_PATH):
        return None
    return json.loads(open(TOKEN_PATH, "r").read())

def is_str(variable):
    if str(type(variable)) == TYE_STR:
        return True
    return False

def is_arr(variable):
    if str(type(variable)) == TYE_LIST:
        return True
    return False

def is_dict(variable):
    if str(type(variable)) == TYE_DICT:
        return True
    return False

def create_automation_package(app_name, basic_automation_detail):
    """
    Creates directory for automation and write jennie.conf.json file in it.
    :param app_name: Application Name
    :param basic_automation_detail: Automation Information.
    :return: True
    """
    os.system("mkdir " + app_name)
    with open('{}/jennie.conf.json'.format(app_name), 'w') as f:
        json.dump(basic_automation_detail, f, indent=2)
    return True