from jennie.constants import *
from jennie.helper import ask_to_select

def map_inputs(arguments):
    args = arguments
    input_selected = AUTOMATION_COMMANDS
    commands = []
    for arg in args:
        if str(type(input_selected)) == "<class 'dict'>":
            if arg not in input_selected:
                print ("Invalid Command, Check Command List at \n\thttps://automations.ask-jennie.com/command-list\n")
                return None, None
            else:
                input_selected = input_selected[arg]
                commands.append(arg)

    while (str(type(input_selected)) == "<class 'dict'>"):
        print ("\n\n")
        input_selected, selected = ask_to_select(input_selected)
        commands.append(selected)

    if input_selected == "library_name" and len(args) > 3:
        commands.append(arguments[3])
    return commands, input_selected
