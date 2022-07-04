"""
event_name : django-automations
config format:
{
    "libs": ["lib1", "lib2"],
    "event_name" : "django-automations"
}
"""

from jennie.constants import *
from jennie.jennietools.api_calls import APICalls

def execute_django_automations(event):
    """
    Execute:
        for each library in libraries.
            run jennie django automations download library
    :param event: {
        "libs": ["NAME_OF_COMPONENT"],
        "event_name" : "django-automations"
    }
    :return: True / False
    """
    for library in event["libs"]:
        os.system("jennie django automations download {}".format(library))
    return True

def validate_django_automations(event):
    """
    validate if libs key is present and hold list of libraries.
    validate all libraries exits on jennie server.
    :param event: {
        "libs": ["NAME_OF_COMPONENT"],
        "event_name" : "django-automations"
    }
    :return: True / False
    """
    if "libs" not in event:
        print("Missing key 'libs' in django-automations event")
        return False

    if str(type(event["libs"])) != "<class 'list'>":
        print("key 'libs' should be a list of libraries")
        return False

    if not APICalls().validate_automations(event["libs"], KEY_STACK_DJANGO_AUTOMATIONS):
        print("All Library in Django Automations does not exits.")
        return False

    return True
