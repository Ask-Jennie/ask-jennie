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
from jennie.rule_engine.events.event_add_ng_library import validate_add_ng_libraries
from jennie.rule_engine.events.event_replace_in_file import validate_replace_in_file

from jennie.rule_engine.events.event_download_files import execute_download_files
from jennie.rule_engine.events.event_create_angular_component import execute_create_angular_component
from jennie.rule_engine.events.event_angular_ui_lib import execute_angular_ui_lib
from jennie.rule_engine.events.event_angular_automations import execute_angular_automations
from jennie.rule_engine.events.event_create_angular_services import execute_create_angular_services
from jennie.rule_engine.events.event_install_npm_library import execute_install_npm_libraries
from jennie.rule_engine.events.event_update_angular_json import execute_update_angular_json
from jennie.rule_engine.events.event_update_angular_modules import execute_update_angular_module
from jennie.rule_engine.events.event_update_angular_routes import execute_update_angular_routes
from jennie.rule_engine.events.event_add_ng_library import execute_add_ng_libraries
from jennie.rule_engine.events.event_replace_in_file import execute_replace_in_file


RuleEngineEvents = {
    KEY_EVENT_DOWNLOAD_FILES: {
        "validate": validate_download_files,
        "execute": execute_download_files,
        "validate_extra_params": ["app_name", "type"]
    },
    KEY_EVENT_CREATE_COMPONENT: {
        "validate": validate_create_angular_component,
        "execute": execute_create_angular_component
    },
    KEY_EVENT_ANGULAR_UI_LIB: {
        "validate": validate_angular_ui_lib,
        "execute": execute_angular_ui_lib
    },
    KEY_EVENT_ANGULAR_AUTOMATIONS: {
        "validate": validate_angular_automations,
        "execute": execute_angular_automations
    },
    KEY_EVENT_ANGULAR_SERVICES: {
        "validate": validate_create_angular_services,
        "execute": execute_create_angular_services
    },
    KEY_EVENT_INSTALL_NPM_LIBRARY: {
        "validate": validate_install_npm_libraries,
        "execute": execute_install_npm_libraries
    },
    KEY_EVENT_UPDATE_ANGULAR_JSON: {
        "validate": validate_update_angular_json,
        "execute": execute_update_angular_json
    },
    KEY_EVENT_UPDATE_ANGULAR_MODULE: {
        "validate": validate_update_angular_module,
        "execute": execute_update_angular_module,
    },
    KEY_EVENT_UPDATE_ANGULAR_ROUTES: {
        "validate": validate_update_angular_routes,
        "execute": execute_update_angular_routes,
        "validate_extra_params": ["app_name", "type"]
    },
    KEY_EVENT_ADD_NG_LIBRARIES: {
        "validate": validate_add_ng_libraries,
        "execute": execute_add_ng_libraries,
    },
    KEY_EVENT_REPLACE_IN_FILE: {
        "validate": validate_replace_in_file,
        "execute": execute_replace_in_file,
    }
}