from jennie.jennie_tools.api_calls import APICalls

def take_user_input(userinputs):
    """
    The method take dict inputs for list of inputs to be taken,
    takes all input from user and returns back input taken
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
        response[key] = input(userinputs[key] + "\n>> ")
    return response

def get_app_name_retry(type, retry_if_found, error_if_not_found, does_app_exits=False):
    if does_app_exits and retry_if_found:
        userinputcancel = input("App name already exits, enter c to cancel or any other key continue")
        if userinputcancel == "c":
            return False, False
        does_app_exits = get_app_name(type)

    elif not does_app_exits and error_if_not_found:
        raise ValueError("App Name Does not exits")

def get_app_name(type, retry_if_found=False, error_if_not_found=False):
    """
    Method takes input from user for app_name and return back app_name
    :param type: type of automation
    :param retry_if_found: ask user to enter different app_name in case app is found on jennie server
    :param error_if_not_found: raise Error in case app is not found on jennie
    :return: App Name
    """

    app_name = input ("Enter App name : \n>> ")
    try:
        does_app_exits = APICalls().automation_validate_api_call(type, app_name)
        if not does_app_exits:
            get_app_name_retry(type, retry_if_found, error_if_not_found)
    except Exception as e:
        get_app_name_retry(type, retry_if_found, error_if_not_found)
    return app_name