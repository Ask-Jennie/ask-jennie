from jennie.constants import *
from getpass import getpass
from jennie.jennietools.api_calls import APICalls
from jennie.jennietools.userinput import take_user_input

__version__ = "0.0.1"
__description__ = 'The package targets protocol for uploading and reusing task and libraries'
__author__ = 'ASK Jennie Developer <saurabh@ask-jennie.com>'

class Setup():
    def __init__(self):
        self.state = 0

    def show_version(self):
        print ("Version :",__version__)
        print ("Author :",__author__)

        print(__description__ + "\n")
        user_info = self.get_logged_in_user()
        if (user_info == None):
            print ("Not logged in, To use the software try login using jennie setup")
            return
        print("User Name :", user_info["fullname"])
        print("User Email :", user_info["email"])

        print ("\nVersion Info : ")
        print ("Stable Version :", user_info["stable"])
        print ("Latest Version :", user_info["latest"])

    def get_logged_in_user(self):
        user_saved_info = None
        userinfo = get_user_access_token()
        if userinfo != None:
            user_saved_info = userinfo["payload"]
        return user_saved_info

    def login_to_ask_jennie(self, email, password):
        response = APICalls().login_api_call(email=email, password=password)
        if (response["payload"] == None):
            print (response["message"])
            return False

        with open(TOKEN_PATH, 'w') as f:
            json.dump(response, f)

        print ("User Logged In Successfully")
        return True

    def setup(self, email=None):
        if email == None:
            info = take_user_input(USER_INPUT_FOR_SETUP)
            email = info["email"]

        self.email = email
        token_info = self.get_logged_in_user()
        if (token_info):
            raise ValueError("User already logged in, try logout to resetup ( jennie logout ) ")
        else:
            print ("Continue Login, Enter Information")
            print ("Input Password for ASK Jennie Email:  ", self.email)
            password = getpass()
            return self.login_to_ask_jennie (self.email, password)

    def logout(self):
        if (self.get_logged_in_user() != None):
            command = "rm -rf {}".format(TOKEN_PATH)
            os.system(command)
            print ("Logged out successfully")
        else:
            print ("User not logged in")
        return True