from jennie.constants import *
from jennie.rule_engine.events.events_mapper import RuleEngineEvents
from jennie.logger import LogginMixin

println = LogginMixin().print

def validate_event_types(automation_conf, automation_type):
    supported = []
    if automation_type == KEY_STACK_ANGULAR_UI_LIB:
        supported = [KEY_EVENT_DOWNLOAD_FILES, KEY_EVENT_CREATE_COMPONENT]
    elif automation_type == KEY_STACK_ANGULAR_AUTOMATION:
        supported = [
            KEY_EVENT_DOWNLOAD_FILES, KEY_EVENT_CREATE_COMPONENT,
            KEY_EVENT_ANGULAR_UI_LIB, KEY_EVENT_ANGULAR_AUTOMATIONS,
            KEY_EVENT_ANGULAR_SERVICES, KEY_EVENT_INSTALL_NPM_LIBRARY,
            KEY_EVENT_UPDATE_ANGULAR_JSON, KEY_EVENT_UPDATE_ANGULAR_MODULE,
            KEY_EVENT_UPDATE_ANGULAR_ROUTES
        ]

    for event in automation_conf:
        curr_event_type = event["event_type"]
        if curr_event_type not in supported:
            print ("Unsupported event {} for automation type {}".format(curr_event_type, automation_type))
            return False
    return True

def execute_events(automation_conf, automation_type):
    validated = validate_event_types(automation_conf, automation_type)
    println ("\n\nAutomation events are validated for type ", automation_type)
    if validated:
        for event in automation_conf:
            println("Running Automation Event: \n\n", json.dumps(event, indent=2), "\n\n")
            println (event[KEY_EVENT_TYPE])
            if event[KEY_EVENT_TYPE] not in RuleEngineEvents:
                raise ("\n\nNot a valid event, check event type")

            RuleEngineEvents[event[KEY_EVENT_TYPE]]["execute"](event)

    return True

def validate_events(automation_conf, automation_type, app_name):
    validated = validate_event_types(automation_conf, automation_type)
    println ("\n\nAutomation events are validated for type ", automation_type, validated, automation_conf)
    validated_events = []
    if validated:
        for event in automation_conf:
            println("Validating Automation Event: \n\n", json.dumps(event, indent=2), "\n\n")
            if event[KEY_EVENT_TYPE] not in RuleEngineEvents:
                raise ("\n\nNot a valid event, check event type")


            if "validate_extra_params" in event:
                if "app_name" in event["validate_extra_params"] and "type" in event["validate_extra_params"]:
                    event_info = RuleEngineEvents[event[KEY_EVENT_TYPE]]["validate"](event, app_name=app_name, type=automation_type)
                elif "app_name" in event["validate_extra_params"]:
                    event_info = RuleEngineEvents[event[KEY_EVENT_TYPE]]["validate"](event, app_name=app_name)
                elif "type" in event["validate_extra_params"]:
                    event_info = RuleEngineEvents[event[KEY_EVENT_TYPE]]["validate"](event, type=automation_type)
                else:
                    event_info = RuleEngineEvents[event[KEY_EVENT_TYPE]]["validate"](event)
            else:
                event_info = RuleEngineEvents[event[KEY_EVENT_TYPE]]["validate"](event)

            if not event_info:
                return False

            if event_info == True:
                event_info = event

            validated_events.append(event_info)
    else:
        print ("Invalid automation events, check if event type is compatible")
        return False
    return validated_events