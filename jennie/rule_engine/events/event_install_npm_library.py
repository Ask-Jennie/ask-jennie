"""
event_name : install-npm-library

config format:
{
    "libs": [],
    "event_name" : install-npm-library
}
"""
import os

def execute_install_npm_libraries(event):
    """
    Install All NPM libraries provided in list in event["libs"]
    :param event: event info
    :return: True
    """
    libs_txt = " ".join(event["libs"])
    os.system("npm i {}".format(libs_txt))
    return True

def validate_install_npm_libraries(event):
    """
    Install All NPM libraries provided in list in event["libs"]
    :param event: event info
    :return: True
    """
    if "libs" not in event:
        print ("No Library present in the event")

    if str(type(event["libs"])) != "<class 'list'>":
        print("key 'libs' should be a list of libraries in event install_npm_libraries")
        return False
    return True