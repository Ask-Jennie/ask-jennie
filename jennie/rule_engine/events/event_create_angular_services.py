"""
event_name : create-angular-services
config format:
{
    "service_name": "NAME_OF_SERVICE",
    "event_name" : create-angular-services
}
"""
import os

def execute_create_angular_services(event):
    """
    Create Angular Service.
    :param event: {
        "component_name": "NAME_OF_SERVICE",
        "event_name" : create-angular-services
    }
    :return: True/False
    """
    os.system("ng g c {}".format(event["service_name"]))
    return True

def validate_create_angular_services(event):
    """
    Validate Angular Services event config.
    :param event: {
        "component_name": "NAME_OF_SERVICE",
        "event_name" : create-angular-services
    }
    :return: True/False
    """
    if "service_name" not in event:
        print ("Missing Service Name name")
        return False

    return True