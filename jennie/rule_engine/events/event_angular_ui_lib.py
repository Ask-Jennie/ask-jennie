"""
event_name : angular-ui-lib
config format:
{
    "libs": ["lib1", "lib2"],
    "event_name" : "angular-ui-lib"
}
"""

from jennie.constants import *
from jennie.jennietools.api_calls import APICalls

def execute_angular_ui_lib(event):
    """
    Execute:
        for each library in libraries.
            run jennie angular ui-lib download library
    :param event: {
        "libs": ["NAME_OF_COMPONENT"],
        "event_name" : "angular-ui-lib"
    }
    :return: True / False
    """
    for library in event["libs"]:
        os.system("jennie angular ui-lib download {}".format(library))
    return True

def validate_angular_ui_lib(event):
    """
    validate if libs key is present and hold list of libraries.
    validate all libraries exits on jennie server.
    :param event: {
        "libs": ["NAME_OF_COMPONENT"],
        "event_name" : "angular-ui-lib"
    }
    :return: True / False
    """
    if "libs" not in event:
        print("Missing key 'libs' in angular ui-lib event")
        return False

    if str(type(event["libs"])) != "<class 'list'>":
        print("key 'libs' should be a list of libraries")
        return False

    # if not APICalls().validate_automations(event["libs"], KEY_STACK_ANGULAR_UI_LIB):
    #     print("All Library in angular ui-lib does not exits.")
    #     return False

    return True
