"""
event_name : adding-npm-library

config format:
{
    "file_contains": "component.ts",
    "event_name" : replace-in-file,
    "find": [""],
    "replace": [""],
    "max_count": 1
}
"""
import os
from jennie.helper import ask_to_select

def find_files(file_contains):
    # folder path
    dir_path = os.getcwd()

    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)) and file_contains in path:
            res.append(path)
    return res


def execute_replace_in_file(event):
    """
    Add NPM libraries provided in list in event["libs"] to project
    :param event: event info
    :return: True
    """
    files = find_files(event["file_contains"])
    if len(files) > event["max_count"]:
        print ("Not a valid directory, the directory should contain max", event["max_count"], "files with", event["file_contains"])
        return False
    selected = files[0]
    if len(files) > 1:
        selected = ask_to_select(files)

    file = open(selected, "rw")
    file_content = file.read()
    for f,r in zip(event["find"], event["replace"]):
        file_content = file_content.replace(f, r)
    return True

def validate_replace_in_file(event):
    """
    Add NPM libraries provided in list in event["libs"]
    :param event: event info
    :return: True
    """
    if "file_contains" not in event:
        print ("File Information field missing 'file_contains'")
        return False

    if "find" not in event:
        print ("Missing find field")
        return False

    if "replace" not in event:
        print ("Missing replace field")
        return False

    if "max_count" not in event:
        event["max_count"] = 1
    return event