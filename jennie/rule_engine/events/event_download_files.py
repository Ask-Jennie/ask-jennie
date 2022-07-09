"""
event_name : download-files
config format:
{
    "files": [{
        file_link: file link from S3 that is required to be downloaded,
        out_path: Output Path where the files has to be uploaded
    }]
}
"""

from jennie.constants import *
from jennie.jennietools.api_calls import APICalls
from jennie.jennietools.replace_image_from_html import replace_local_images


def execute_download_files(event):
    """
    Download and save list of file to provided location.
    :param files: [{
        file_link: file link from S3 that is required to be downloaded,
        out_path: Output Path where the files has to be uploaded
    }]
    :return: True
    """
    for fileinfo in event["files"]:
        file_link, out_path = fileinfo[KEY_FILE_LINK], fileinfo[KEY_OUT_PATH]
        file_content = APICalls().download_text_file(file_link)
        open(out_path, "w").write(file_content)
    return True


def validate_download_files(event, type, app_name):
    """
    validate if libs key is present and hold list of libraries.
    validate all libraries exits on jennie server.
    :param event: {
        "libs": ["NAME_OF_COMPONENT"],
        "event_name" : "django-automations"
    }
    :return: True / False
    """
    if "files" not in event:
        print("Missing key 'files' in download-files event")
        return False

    for fileinfo in event["files"]:
        if KEY_OUT_PATH not in fileinfo:
            print("Missing key '{}' in one of the events of download files".format(KEY_OUT_PATH))

        if KEY_FILE_PATH not in fileinfo:
            print("Missing key '{}' in one of the events of download files".format(KEY_FILE_PATH))
        else:
            print (fileinfo[KEY_FILE_PATH], app_name, type)
            replace_local_images(fileinfo[KEY_FILE_PATH])
            fileinfo[KEY_FILE_LINK] = APICalls().upload_text_file(
                fileinfo[KEY_FILE_PATH],
                app_name=app_name,
                type=type
            )[KEY_FILE_LINK]
            del fileinfo[KEY_FILE_PATH]

    return event
