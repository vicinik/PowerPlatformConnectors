# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------
"""
List command.
"""

from paconn import _LIST

from paconn.common.util import display
from paconn.settings.util import load_powerapps_and_flow_rp
from paconn.settings.settingsbuilder import SettingsBuilder

_PROPERTIES = 'properties'
_VALUE = 'value'
_DISPLAY_NAME = 'displayName'
_IS_CUSTOM_API = 'isCustomApi'
_NAME = 'name'

# pylint: disable=too-many-arguments
def list(environment):
    """
    List command.
    """
    # Get settings
    settings = SettingsBuilder.get_settings(
        environment=environment,
        settings_file=None,
        api_properties=None,
        api_definition=None,
        icon=None,
        script=None,
        connector_id=None,
        powerapps_url=None,
        powerapps_version=None)

    powerapps_rp, _ = load_powerapps_and_flow_rp(
        settings=settings,
        command_context=_LIST)

    connectors_val = powerapps_rp.get_all_connectors(settings.environment)
    connectors_list = connectors_val[_VALUE]
    custom_connectors = filter(lambda conn: conn[_PROPERTIES][_IS_CUSTOM_API], connectors_list)

    conn_str = "Connectors:\n"
    for conn in custom_connectors:
        conn_str += conn[_NAME] + '|' + conn[_PROPERTIES][_DISPLAY_NAME] + '\n'

    print(conn_str)
