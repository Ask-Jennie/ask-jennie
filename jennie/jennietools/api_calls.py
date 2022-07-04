import requests
from jennie.constants import get_user_access_token
from jennie.jennietools.api_urls import *
from jennie.logger import LogginMixin

println = LogginMixin().print

class APICalls():
    """
    Simply library to simplify API Calls using python.
    """
    def recreate_url(self, url, params):
        split_keyword = "?"
        for key in params:
            url += split_keyword + key + "=" + params[key]
            split_keyword = "&"
        return url

    def get(self, url, headers=None, params=None):
        """
        Make a get api call, if params are present add params to url,
        if headers are present add headers to requests
        :param url: Request URL
        :param headers: Request Headers ( optional )
        :param params: Request Params ( optional )
        :return: API Call JSON Response.
        """
        if params != None:
            url = self.recreate_url(url, params)

        if headers == None:
            headers = {"Content-type": "application/json"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_text(self, url, params=None):
        """
        Make a get api call, if params are present add params to url,
        if headers are present add headers to requests
        :param url: Request URL
        :param headers: Request Headers ( optional )
        :param params: Request Params ( optional )
        :return: API Call JSON Response.
        """
        if params != None:
            url = self.recreate_url(url, params)

        response = requests.get(url)
        return response.text

    def post(self, url, headers=None, body=None):
        """
        Make a post api call, if headers are present add headers to requests, if body is present
        :param url: Request URL
        :param headers: Request Headers ( optional )
        :param body: Request Params ( optional )
        :return: API Call JSON Response.
        """
        if headers == None:
            headers = {"Content-type": "application/json"}

        if body == None:
            body = {}

        response = requests.post(url, headers=headers, json=body)
        return response.json()

    def put(self, url, headers=None, body=None):
        """
        Make a put api call, if headers are present add headers to requests, if body is present
        :param url: Request URL
        :param headers: Request Headers ( optional )
        :param body: Request Params ( optional )
        :return: API Call JSON Response.
        """
        if headers == None:
            headers = {"Content-type": "application/json"}

        if body == None:
            body = {}
        response = requests.put(url, headers=headers, json=body)
        return response.json()

    def delete(self, url, headers=None, body=None):
        """
        Make a delete api call, if headers are present add headers to requests, if body is present
        :param url: Request URL
        :param headers: Request Headers ( optional )
        :param body: Request Params ( optional )
        :return: API Call JSON Response.
        """
        if headers == None:
            headers = {"Content-type": "application/json"}

        if body == None:
            body = {}
        response = requests.delete(url, headers=headers, json=body)
        return response.json()


    # Helper Functions
    def login_api_call(self, email, password):
        """
        API call to login to ASK Jennie
        :param email: user email address
        :param password: user password
        :return: API Call response JSON.
        """
        api_url = LOGIN_URL
        body = {"email": email, "password": password}
        response = self.post(url=api_url, body=body)
        return response

    def validate_automation_api_call(self, type, app_name):
        """
        Validate if type of automation already exits on ASK jennie Server
        :param type: Type of automation
        :param app_name: Automation name
        :return: True/False
        """
        api_url = AUTOMATION_VALIDATE_URL.replace("TYPE", type)

        headers = { "token": get_user_access_token()["payload"]["token"] }
        response = self.get(api_url, headers, params={"app_name": app_name})
        println(response)
        if not response["payload"]:
            return False
        return True

    def validate_automations(self, type, libs):
        """
        Validate if type of automation already exits on ASK jennie Server
        :param type: Type of automation
        :param app_name: Automation name
        :return: True/False
        """
        api_url = AUTOMATION_VALIDATE_URL.replace("TYPE", type)

        headers = { "token": get_user_access_token()["payload"]["token"] }
        response = self.post(api_url, headers, body={"libs": libs})
        print("Api Response, ", response)
        if not response["payload"]:
            return False
        return True

    def upload_automation_api_call(self, type, json_conf):
        """
        Add Type of automation to ASK Jennie server
        :param type: Type of automation
        :param json_conf: automation configration.
        :return: API Call response JSON.
        """
        api_url = AUTOMATION_URL.replace("TYPE", type)
        headers = {"token": get_user_access_token()["payload"]["token"] }
        response = self.post(api_url, headers, body=json_conf)
        if response["payload"] == False:
            print ("Error While uploading automation")
            return None

        return response

    def download_automation_api_call(self, type, app_name):
        """
        Download Automation from ASK Jennie
        :param type: type of automation
        :param app_name: App name to download
        :return: API Call response JSON.
        """
        api_url = AUTOMATION_URL.replace("TYPE", type)
        headers = {"token": get_user_access_token()["payload"]["token"] }
        response = self.get(api_url, headers, params={"app_name": app_name})
        return response

    def update_automation_api_call(self, type, json_conf):
        """
        Update ASK Jennie automation that is already present on Server.
        :param type: Type of automation
        :param json_conf: automation configration.
        :return:
        """
        api_url = AUTOMATION_URL.replace("TYPE", type)
        headers = {"token": get_user_access_token()["payload"]["token"] }
        response = self.put(api_url, headers, body=json_conf)
        return response

    def delete_automation_api_call(self, type, app_name):
        """
        Update ASK Jennie automation that is already present on Server.
        :param type: Type of automation
        :param json_conf: automation configration.
        :return:
        """
        api_url = AUTOMATION_URL.replace("TYPE", type)
        headers = {"token": get_user_access_token()["payload"]["token"] }
        response = self.delete(api_url, headers, body={"app_name": app_name})
        return response

    def validate_custom_automation_api_call(self, type, app_name):
        """
        Validate if type of automation already exits on ASK jennie Server
        :param type: Type of automation
        :param app_name: Automation name
        :return: True/False
        """
        api_url = CUSTOM_AUTOMATION_VALIDATE_URL.replace("TYPE", type)

        headers = { "token": get_user_access_token()["payload"]["token"] }
        response = self.get(api_url, headers, params={"app_name": app_name})
        print("Api Response, ", response)
        if not response["payload"]:
            return False
        return True

    def download_custom_automation_api_call(self, type, app_name):
        """
        Download Automation from ASK Jennie
        :param type: type of automation
        :param app_name: App name to download
        :return: API Call response JSON.
        """
        api_url = CUSTOM_AUTOMATION_URL.replace("TYPE", type)
        headers = {"token": get_user_access_token()["payload"]["token"] }
        response = self.get(api_url, headers, params={"app_name": app_name})
        return response


    # Normal Upload and Download Functions

    def upload_image(self, image_file_path):
        """
        Upload Image File to Server
        :param image_file_path: Local path for image
        :return: Uploaded File path
        """
        files = {'media': open(image_file_path, 'rb')}
        image_res = requests.post(IMAGE_UPLOAD_API, headers={"token": get_user_access_token()["payload"]["token"]},
                                  files=files)
        return image_res.json()["payload"]

    def upload_text_file(self, text_file_path, app_name, type):
        """
        Upload text file to ASK Jennie Server
        :param text_file_path: Local path for text file.
        :param app_name: Application name
        :param type: Type of application
        :return: Uploaded File path
        """
        json_content = {
            "file_content": open(text_file_path, 'r').read(),
            "app_name": app_name,
            "filename": text_file_path.split("/")[-1],
            "type": type
        }
        text_res = requests.post(TEXT_UPLOAD_API, headers={"token": get_user_access_token()["payload"]["token"]},
                                 json=json_content)
        return text_res.json()["payload"]

    def download_text_file(self, file_url):
        """
        Download File from specific URL.
        :param file_url: FILE URL
        :return: content of file.
        """
        return self.get_text(file_url)
