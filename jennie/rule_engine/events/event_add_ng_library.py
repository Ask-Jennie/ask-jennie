"""
event_name : adding-npm-library

config format:
{
    "libs": [],
    "event_name" : adding-npm-library
}
"""
import os

def execute_add_ng_libraries(event):
    """
    Add NPM libraries provided in list in event["libs"] to project
    :param event: event info
    :return: True
    """
    for key in event["libs"]:
        os.system("ng add {}".format(key))
    return True

def validate_add_ng_libraries(event):
    """
    Add NPM libraries provided in list in event["libs"]
    :param event: event info
    :return: True
    """
    if "libs" not in event:
        print ("No Library present in the event")

    if str(type(event["libs"])) != "<class 'list'>":
        print("key 'libs' should be a list of libraries in event install_npm_libraries")
        return False
    return event