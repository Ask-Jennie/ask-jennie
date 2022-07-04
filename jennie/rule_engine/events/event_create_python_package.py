"""
event_name : "create-python-package"
config format:
{
    "package_dir": "directory path for the package",
    "event_name" : "create-python-package"
}
"""
import os

def execute_create_python_package(event):
    """
    Create Python package, directory with constructor file (__init__.py)
    :param event:
    {
        "package_dir": "directory path for the package",
        "event_name" : "create-python-package"
    }
    :return: True/False
    """
    os.system("mkdir {}".format(event["package_dir"]))
    os.system("touch {}/__init__.py".format(event["package_dir"]))
    return True

def validate_create_python_package(event):
    """
    Validate Event create python package.
    :param event:
    {
        "package_dir": "directory path for the package",
        "event_name" : "create-python-package"
    }
    :return: True/False
    """
    if "package_dir" not in event:
        print("Missing package_dir key in create_python_package event.")
        return False
    return True