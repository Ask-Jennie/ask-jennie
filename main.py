class LogginMixin():
    def __init__(self):
        self.debug = True

    def function_1(self, event_info):
        print ("function_1", event_info)
        return True

    def function_2(self, event_info):
        print ("function_2", event_info)
        return True

if __name__ == '__main__':
    logger_mixn = LogginMixin()
    Mapper = {
        "install-npm": logger_mixn.function_1,
        "install-libs": logger_mixn.function_2,
    }
    events = [
        {"someinfo": "some", "event_type": "install-npm"},
        {"someinfo": "213423412", "event_type": "install-libs"}
    ]
    print (Mapper[events[0]["event_type"]](events[0]))
    print (Mapper[events[1]["event_type"]](events[1]))