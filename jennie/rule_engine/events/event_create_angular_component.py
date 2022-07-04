"""
event_name : create-angular-component
config format:
{
    "component_name": "NAME_OF_COMPONENT",
    "event_name" : create-angular-component
}
"""
import os
from jennie.logger import LogginMixin

println = LogginMixin().print

def execute_create_angular_component(event):
    """
    Create Angular Component.
    :param event: {
        "component_name": "NAME_OF_COMPONENT",
        "event_name" : create-angular-component
    }
    :return: True/False
    """
    command = "ng g c {}".format(event["component_name"])
    println ("Running command : ", command)
    os.system(command)
    return True

def validate_create_angular_component(event):
    """
    Validate Angular component event config.
    :param event: {
        "component_name": "NAME_OF_COMPONENT",
        "event_name" : create-angular-component
    }
    :return: True/False
    """
    if "component_name" not in event:
        print ("Missing component name")
        return False

    return True