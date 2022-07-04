from jennie.jennietools.api_calls import APICalls
from jennie.constants import *
from jennie.logger import *

println = LogginMixin().print

def take_user_input(userinputs, default_values=None):
    """
    The method take dict inputs for list of inputs to be taken,
    takes all input from user and returns back input taken
    :param default_values: Provide default values for key.
    If default values are provided user is asked for update.
    {
        "key": "value"
    }
    :param inputs: Format for dict
    {
        "key": "Description to be show for input"
    }
    :return:
    {
        "key": "[INPUT_FROM_USER]"
    }
    """
    response = { }
    for key in userinputs:
        if default_values and key in default_values:
            confirm = input("Do you want to update information for {} (Y/N) ".format(key))
            if confirm.lower() == "y" or confirm.lower() == "yes":
                response[key] = input(userinputs[key] + "\n>> ")
            else:
                response[key] = default_values[key]
        else:
            response[key] = input(userinputs[key] + "\n>> ")
    return response

def get_ask_app_name(type, app_name=None):
    """
    Get app name and check if app name exits on jennie server or not
    :param type: Type of automation
    :param app_name: Application name, if none, ask for application name
    :return: app_exits, app_name
    """
    println("get_ask_app_name: type, app_name = ", type, app_name)
    while(app_name == None):
        app_name = input("Enter App name (Make sure app name is unique under {} category): \n>> ".format(type))
        if len(app_name) < 3:
            app_name = None
    try:
        does_app_exits = APICalls().validate_automation_api_call(type, app_name)
    except Exception as e:
        print ("Exceptions occured:", e)
        raise ValueError("Unhandled API Exception, unable to validate {} automation with name {} on server ".format(type, app_name))
    return does_app_exits, app_name

def get_basic_automation_conf(app_name, type, stack, default_inputs=None):
    configuration = {
        "app_name": app_name
    }

    user_input = take_user_input(AUTOMATION_BASIC_INPUT, default_inputs)
    for key in user_input:
        configuration[key] = user_input[key]

    if default_inputs == None:
        configuration["automation_conf"] = []
        configuration["stack"] = stack
        configuration["type"] = type
        configuration["app_image"] = ""
        if type == "angular-ui-lib":
            configuration["dependencies"] = ["bootstrap-5"]
        else:
            configuration["dependencies"] = []
    return configuration



def get_app_image():
    image_info = take_user_input({
        "app_image": "Input path for application image"
    })
    return image_info["app_image"]