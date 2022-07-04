from jennie.constants import *
from jennie.rule_engine.events.event_download_files import execute_download_files
from jennie.rule_engine.events.event_create_angular_component import execute_create_angular_component
from jennie.rule_engine.events.event_angular_ui_lib import execute_angular_ui_lib
from jennie.rule_engine.events.event_angular_automations import execute_angular_automations
from jennie.rule_engine.events.event_create_angular_services import execute_create_angular_services
from jennie.rule_engine.events.event_install_npm_library import execute_install_npm_libraries
from jennie.rule_engine.events.event_update_angular_json import execute_update_angular_json
from jennie.rule_engine.events.event_update_angular_modules import execute_update_angular_module
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
            if event[KEY_EVENT_TYPE] == KEY_EVENT_DOWNLOAD_FILES:
                execute_download_files(event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_CREATE_COMPONENT:
                execute_create_angular_component(event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_ANGULAR_UI_LIB:
                execute_angular_ui_lib(event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_ANGULAR_AUTOMATIONS:
                execute_angular_automations(event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_ANGULAR_SERVICES:
                execute_create_angular_services(event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_INSTALL_NPM_LIBRARY:
                print ("Installing NPM Dependencies")
                execute_install_npm_libraries(event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_UPDATE_ANGULAR_JSON:
                execute_update_angular_json(angular_json_filepath="angular.json", event=event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_UPDATE_ANGULAR_MODULE:
                print ("Updating Angular Module")
                execute_update_angular_module(angular_module_file_path="src/app/app.module.ts", event=event)
            elif event[KEY_EVENT_TYPE] == KEY_EVENT_UPDATE_ANGULAR_ROUTES:
                execute_update_angular_module(event=event, angular_module_file_path="src/app/app-routing.module.ts")
            else:
                println("\nUnknown Event =============")
    return True