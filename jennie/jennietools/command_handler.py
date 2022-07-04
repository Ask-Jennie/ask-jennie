from jennie.constants import *

def ask_to_select(inputs):
    input_arr = []
    for key in inputs:
        input_arr.append(key)

    idx = 1
    print ("Select Subcommand ...")
    for key in input_arr:
        print (str(idx) + ". " + key)
        idx += 1

    try:
        selected = int(input(">>"))
        return inputs[input_arr[selected-1]], input_arr[selected-1]
    except Exception as e:
        print ("Invalid Option try selecting again")
        return ask_to_select(inputs)

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
