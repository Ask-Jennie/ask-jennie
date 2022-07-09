from jennie.configration import IS_LOGGER_ACTIVE
class LogginMixin():
    def __init__(self):
        self.debug = IS_LOGGER_ACTIVE

    def print(self, *args):
        string = ""
        for key in args:
            string += str(key) + " "

        if self.debug:
            print(string)
        return True