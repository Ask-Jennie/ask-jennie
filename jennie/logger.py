class LogginMixin():
    def __init__(self):
        self.debug = True

    def print(self, *args):
        string = ""
        for key in args:
            string += str(key) + " "

        if self.debug:
            print(string)
        return True