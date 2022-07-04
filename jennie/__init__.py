import sys
from jennie.jennietools.command_handler import map_inputs
from jennie.jennietools.userinput import take_user_input
from jennie.setup import Setup
from jennie.ubuntu import UbuntuAutomation
from jennie.automations.angularuilib import AngularUILib
from jennie.automations.angularautomations import AngularAutomations
from jennie.logger import LogginMixin

println = LogginMixin().print

def check_user_setup():
    """
    Check if user is logged in.
    :return: User Logged In Info, login status
    """
    setup_controller = Setup()
    is_user_logger_in = False
    userinfo = setup_controller.get_logged_in_user()
    if userinfo != None:
        is_user_logger_in = True

    return userinfo, is_user_logger_in, setup_controller

def perform_task_non_logged_in_user(commands, setup_controller):
    """
    Non logged in user have access only to setup and version command.
    :return: True
    """
    user_email = None
    if commands[0] == "setup" and len(commands) > 1:
        user_email = commands[1]
        return setup_controller.setup(user_email)

    elif commands[0] == "version" or commands[0] == "--version":
        return setup_controller.show_version()

    else:
        print ("User not logged in, To use jennie kindly login to the software.\n"
               "To Login use command"
               "\n\n\tjennie setup <user-email>\n"
               "Once logged in user can continue using jennie")


def run():
    commands, input_selected = map_inputs(sys.argv[1:])
    println ("Map Input Running.....")
    println (commands, input_selected)
    if commands == None:
        return False

    userinfo, is_user_logger_in, setup_controller = check_user_setup()
    if not is_user_logger_in:
        return perform_task_non_logged_in_user(commands, setup_controller)

    # Run ubuntu automations.
    elif commands[0] == "ubuntu":
        UbuntuAutomation().execute(commands)

    # Run Angular UI-Lib protocol.
    elif commands[0] == "angular" and commands[1] == "ui-lib":
        resp = AngularUILib(commands, userinfo).execute

    # Run Angular Automation Protocol.
    elif commands[0] == "angular" and commands[1] == "automations":
        resp = AngularAutomations(commands, userinfo).execute