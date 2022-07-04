from jennie.constants import *
from jennie.rule_engine.events.event_download_files import validate_download_files
from jennie.rule_engine.events.event_create_angular_component import validate_create_angular_component
from jennie.rule_engine.events.event_angular_ui_lib import validate_angular_ui_lib
from jennie.rule_engine.events.event_angular_automations import validate_angular_automations
from jennie.rule_engine.events.event_create_angular_services import validate_create_angular_services
from jennie.rule_engine.events.event_install_npm_library import validate_install_npm_libraries
from jennie.rule_engine.events.event_update_angular_json import validate_update_angular_json
from jennie.rule_engine.events.event_update_angular_modules import validate_update_angular_module
from jennie.rule_engine.events.event_update_angular_routes import validate_update_angular_routes
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

def validate_events(automation_conf, automation_type, app_name):
    validated = validate_event_types(automation_conf, automation_type)
    println ("\n\nAutomation events are validated for type ", automation_type, validated, automation_conf)
    validated_events = []
    if validated:
        for event in automation_conf:
            println("Validating Automation Event: \n\n", json.dumps(event, indent=2), "\n\n")
            if event[KEY_EVENT_TYPE] == KEY_EVENT_DOWNLOAD_FILES:
                event_info = validate_download_files(
                    event=event,
                    type=automation_type,
                    app_name=app_name
                )
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False

                validated_events.append(event_info)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_CREATE_COMPONENT:
                event_info = validate_create_angular_component(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False

                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_ANGULAR_UI_LIB:
                event_info = validate_angular_ui_lib(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_ANGULAR_AUTOMATIONS:
                event_info = validate_angular_automations(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_ANGULAR_SERVICES:
                event_info = validate_create_angular_services(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_INSTALL_NPM_LIBRARY:
                event_info = validate_install_npm_libraries(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_UPDATE_ANGULAR_JSON:
                event_info = validate_update_angular_json(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_UPDATE_ANGULAR_MODULE:
                event_info = validate_update_angular_module(event)
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event)

            elif event[KEY_EVENT_TYPE] == KEY_EVENT_UPDATE_ANGULAR_ROUTES:
                event_info = validate_update_angular_routes(
                    event, app_name=app_name,
                    type=automation_type
                )
                if event_info == False:
                    print ("There is some problem with the event ", event[KEY_EVENT_TYPE])
                    return False
                validated_events.append(event_info)
    else:
        print ("Invalid automation events, check if event type is compatible")
    return validated_events