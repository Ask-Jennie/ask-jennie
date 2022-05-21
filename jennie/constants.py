import requests, os, json

API_BASE = "https://api.ask-jennie.com/v1/"
IMAGE_UPLOAD_API = API_BASE + "/image_upload/"
TEXT_UPLOAD_API = API_BASE + "file_upload/"
LOGIN_API = API_BASE + "login/"

KEY_ANGULAR_AUTOMATION = "angular-automation"
KEY_ANGULAR_UI_LIB = "angular-ui-lib"
KEY_DOWNLOAD_FILES = "download_files"
KEY_ANGULAR_ROUTES = "angular_routes"
KEY_NPM_COMMANDS = "npm_commands"
KEY_INDEX_SCRIPT = "index_script"
KEY_INDEX_CSS = "index_css"
KEY_KEY = "key"
KEY_LIBRARIES = "libraries"
KEY_FILES = "files"
KEY_FILE_LINK = "file_link"
KEY_COMPONENT_NAME = "component_name"
KEY_COMPONENT_PATH = "component_path"
KEY_FILEPATH = "filepath"

USER_INPUT_FOR_SETUP = {
    "email": "Kindly enter email address registered with ASK jennie, \nDon't have account go to https://ask-jennie.com/register"
}


AUTOMATION_COMMANDS = {
    "ubuntu": {
        "setup": ["lemp", "phpmyadmin", "elk", "elasticsearch"],
        "deploy": ["django", "web"]
    },
    "angular": {
        "ui-lib": ["upload", "download", "update", "delete"],
        "automations": [
            "add-user-session",
            "add-api",
            "add-firebase-firestore",
            "add-firebase-storage",
            "add-firebase-realtimedb",
            "add-airtable-api"
        ]
    },
    "django": {
        "automations": {
            "create-api",
            "structure-django",
            "add-logs-manager",
            "add-auth-gaurd",
            "create-model",
            "create-controller",
            "create-view"
        }
    },
    "logout": "",
    "version": ""
}

SETUP_COMMANDS = {
    "setup": "",
    "version": ""
}

DEPLOY_INFO_COMMANDS = {
    "port": "Input port no to which the project has to be deployed",
    "domain": "Input your domain name, can add IP address as domain name"
}

ANGULAR_UI_INFO_INPUT_KEYS = {
    "app_title": "Title for UI module",
    "app_description": "Description for UI module",
    "app_image": "Image file path, complete path of image",
    "tag": "Tag (optional) for module",
}

ANGULAR_UI_INFO_INPUT_2_KEYS = {
    "app_title": "Title for UI module",
    "app_description": "Description for UI module",
    "tag": "Tag (optional) for module",
}

ANGULAR_UI_KEYS = {
    "app_title": "Title for UI module",
    "app_description": "Description for UI module",
    "tag": "Tag (optional) for module",
}


SAMPLE_ANGULAR_AUTOMATION_CONF = [
    {
        "type": KEY_DOWNLOAD_FILES,
        "files": {
            KEY_FILE_LINK: "filepath",
            KEY_FILEPATH: "filepath_1",
        }
    },
    {
        "type": "ui-lib", "libraries": []
    },
    {
        "type": "angular-automations", "automations": []
    },
    {
        "type": "add_routes",
        "routes": [{ "component_name": "", "component_path": "", "AuthGaurd": False }]
    },
    {
        "type": "index_script",
        "script": [ ]
    },
    {
        "type": "index_css",
        "script": [ ]
    }
]

SAMPLE_ANGULAR_UI_LIB_CONF = {
    "component_css_file": "",
    "component_html_file": "",
    "component_ts_file": "",
    "scripts": []
}

ANGULAR_AUTOMATION_TYPES = [
    KEY_ANGULAR_AUTOMATION, KEY_ANGULAR_UI_LIB, KEY_DOWNLOAD_FILES,
    KEY_ANGULAR_ROUTES, KEY_NPM_COMMANDS, KEY_INDEX_SCRIPT,
    KEY_INDEX_CSS, KEY_KEY, KEY_LIBRARIES, KEY_FILES
]

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

def get_basic_user_input(type, take_app_name=True):
    name = str(type).replace("-", " ").capitalize()
    key_user_inputs = {}

    if take_app_name:
        key_user_inputs["app_name"] = "Some application name, should be unique and must not include any special character"

    key_user_inputs["app_title"] = "Title for " + name
    key_user_inputs["app_description"] = "Description for " + name

    return key_user_inputs
