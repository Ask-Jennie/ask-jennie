from jennie.constants import *
from jennie.jennie_tools.userinput import take_user_input
from jennie.setup import Setup
from jennie.jennie_tools.custom_exception_handler import return_error

__version__ = "0.0.1"
__description__ = 'The package targets protocol for uploading and reusing task and libraries'
__author__ = 'ASK Jennie Developer <saurabh@ask-jennie.com>'

class CommandHandler():
    def __init__(self):
        self.setup = Setup()
        self.is_user_logged_in = self.setup.is_user_logged_in()

    def show_version(self):
        self.setup.show_version(
            __author__=__author__,
            __version__=__version__,
            __description__=__description__
        )

    def process_command(self, command):
        if not command:
            return False

        if not self.is_user_logged_in:
            if command[0] == "setup":
                info = take_user_input(USER_INPUT_FOR_SETUP)
                self.setup.setup(info["email"])
                return True, None, False
            elif command[0] == "version":
                self.show_version()
                return True, None, False
            else:
                return return_error("You must log in before using any feature from ASK Jennie.")
        else:
            if command[0] == "logout":
                self.setup.logout()
                return None, None, False
            elif command[0] == "version":
                self.show_version()
                return True, None, False
            else:
                return command, self.is_user_logged_in, True

    def start(self, arguments):
        if not self.is_user_logged_in:
            commands = SETUP_COMMANDS
        else:
            commands = AUTOMATION_COMMANDS
        if len(arguments) == 1 and arguments[0] == "show_commands":
            return MapCommands(commands).show_commands(self.is_user_logged_in)
        command = MapCommands(commands).map(arguments, self.is_user_logged_in)
        return self.process_command(command)

    @property
    def help(self):
        return MapCommands(None).show_commands(self.is_user_logged_in)

class MapCommands():
    def ask_user_to_select(self, options):
        """
        Takes options paramters as array and allow user to select one of then.
        eg options = ["Option 1", "Option 2"]
        output
        >> press 1 Option 1
        >> press 2 Option 2
        and returns back selected option
        :param options:
        :return:
        """
        counter = 1
        for option in options[:20]:
            print("\tpress " + str(counter) + " for " + str(option))
            counter += 1

        user_selection = input(">> ")
        try:
            return options[int(user_selection) - 1]
        except Exception as e:
            print("Invalid User Input Try again")
            self.ask_user_to_select(options)

    def __init__(self, commands):
        """
        {
            "plot": {
                "fft": ["wav-file", "json-file", "firebase-storage"]
                "spectrum": ["wav-file", "json-file", "firebase-storage"]
            },
            "convert": {
                "json-to-wav": ["json-file", "firebase-storage"]
            },
            "firebase-storage": ["show-device-performance-info", "failed-logs"]
        }

        executed commands could be
            plot fft wav-file
            plot fft json-file
            plot fft firebase-storage
            and so on.

        if user has entered option_1
            show in option to select between option_1_1, option_1_2
            based on above show inside.
        :param commands:
        """
        self.commands = commands
        self.all_commands = []

    def show_commands(self, is_user_logged_in):
        '''
            Takes user login status and print commands available.
        '''
        if not is_user_logged_in:
            print("1. jennie setup")
            print("2. jennie version")
            return return_error("To Use jennie feature you must login using setup command")
        else:
            all_commands = []
            def fetch_from_arr(arr, all_commands, level=2, stack=None):
                for type in arr:
                    if level == 3:
                        all_commands.append(
                            "jennie {} {} {}".format(platform, stack, type)
                        )
                    elif level == 2:
                        all_commands.append(
                            "jennie {} {}".format(platform, type)
                        )
                return all_commands

            for platform in AUTOMATION_COMMANDS:
                if is_arr(AUTOMATION_COMMANDS[platform]):
                    all_commands = fetch_from_arr(platform, all_commands)
                else:
                    for stack in AUTOMATION_COMMANDS[platform]:
                        if is_arr(AUTOMATION_COMMANDS[platform][stack]):
                            all_commands = fetch_from_arr(AUTOMATION_COMMANDS[platform][stack], all_commands, level=3, stack=stack)
            counter = 1
            print ("\nAvailable Commands\n")
            for key in all_commands:
                print ("{}. {}".format(str(counter), key))
                counter += 1
            return return_error("\nUser Login Status : True\n")

    def map(self, inputs, is_user_logged_in):
        current_command = self.commands
        for i in range(0, len(inputs)):
            if is_dict(current_command) and inputs[i] in current_command:
                current_command = current_command[inputs[i]]
            elif is_arr(current_command) and inputs[i] in current_command:
                return inputs
            else:
                if not is_user_logged_in:
                    print ("Invalid Command. check command list using jennie show-commands")
                    print("1. jennie setup")
                    print("2. jennie version")
                    return return_error("To Use jennie feature you must login using setup command")
                else:
                    print ("Invalid Command. check command list using jennie show-commands")
                    print("1. jennie ubuntu setup lemp")
                    print("2. jennie ubuntu setup phpmyadmin")
                    print("3. jennie ubuntu setup elasticsearch")
                    print("4. jennie ubuntu setup elk")
                    print("5. jennie ubuntu deploy django")
                    print("6. jennie ubuntu deploy web")
                    print("7. jennie angular ui-lib download")
                    print("8. jennie angular ui-lib upload")
                    print("9. jennie angular ui-lib update")
                    print("10. jennie angular ui-lib delete")
                    print("11. jennie logout")
                    print("12. jennie version")
                    return return_error("Try using any of the above command")

        if is_arr(current_command):
            current_input = self.ask_user_to_select(current_command)
            inputs.append(current_input)

        elif is_dict(current_command):
            list_commands = []
            for command in current_command:
                list_commands.append(command)

            current_input = self.ask_user_to_select(list_commands)
            inputs.append(current_input)
            self.map(inputs, is_user_logged_in)

        return inputs