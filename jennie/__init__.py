import sys
from jennie.jennie_tools.command_handler import *
from jennie.ubuntu import *
from jennie.angular import *

def execute():
    arguments = sys.argv[1:]
    pre_command_str = "-".join(arguments)

    if pre_command_str == "ubuntu-setup-elk":
        setup_elasticsearchkibana()
        return
    elif pre_command_str == "ubuntu-setup-elasticsearch":
        setup_elasticsearch()
        return
    elif pre_command_str == "ubuntu-setup-lemp":
        setup_lemp()
        return
    elif pre_command_str == "ubuntu-setup-phpmyadmin":
        install_phpmyadmin()
        return
    elif pre_command_str == "ubuntu-deploy-web":
        info = take_user_input(DEPLOY_INFO_COMMANDS)
        deploy_folder_nginx(info["port"], info["domain"])
        return
    elif pre_command_str == "ubuntu-deploy-django":
        info = take_user_input(DEPLOY_INFO_COMMANDS)
        deploy_django(info["port"], info["domain"])
        return

    if len(arguments) > 0 and (arguments[0] == "help" or arguments[0] == "--help"):
        resp = CommandHandler().help
        return

    response = CommandHandler().start(arguments)
    if not response:
        return

    commands, user_info, continue_process = response
    if not continue_process:
        return

    command_str = "-".join(commands)
    token = user_info["token"]

    if command_str == "ubuntu-setup-elk":
        setup_elasticsearchkibana()
    elif command_str == "ubuntu-setup-elasticsearch":
        setup_elasticsearch()
    elif command_str == "ubuntu-setup-lemp":
        setup_lemp()
    elif command_str == "ubuntu-setup-phpmyadmin":
        install_phpmyadmin()
    elif command_str == "ubuntu-deploy-web":
        info = take_user_input(DEPLOY_INFO_COMMANDS)
        deploy_folder_nginx(info["port"], info["domain"])
    elif command_str == "ubuntu-deploy-django":
        info = take_user_input(DEPLOY_INFO_COMMANDS)
        deploy_django(info["port"], info["domain"])

    elif command_str == "angular-ui-lib-upload":
        status = AngularUILibModule(token).upload
    elif command_str == "angular-ui-lib-download":

        status = AngularUILibModule(token).download
    elif command_str == "angular-ui-lib-update":
        status = AngularUILibModule(token).update
    elif command_str == "angular-ui-lib-delete":
        status = AngularUILibModule(token).delete

if __name__ == '__main__':
    execute()