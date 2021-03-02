#!/usr/bin/python
# -*- coding: utf-8 -*-
# © Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_radius_server
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community',
    'license': 'Apache 2.0'
}

DOCUMENTATION = """
---
module: sonic_radius_server
version_added: "1.0.0"
author: "Niraimadaiselvam M (@niraimadaiselvamm)"
short_description: Configures radius server settings on Enterprise SONiC.
description:
  - This module provides configuration management of radius server parameters on devices running Enterprise SONiC.
options:
  config:
    description:
      - Specifies the radius server related configuration.
    type: dict
    suboptions:
      auth_type:
        description:
          - Specifies the authencation type of the radius server.
        type: str
        choices:
          - pap
          - chap
          - mschapv2
        default: pap
      key:
        description:
          - Specifies the key of the radius server.
        type: str
      nas_ip:
        description:
          - Specifies the network access server of the radius server.
        type: str
      statistics:
        description:
          - Specifies the statistics flag of the radius server.
        type: bool
      timeout:
        description:
          - Specifies the timeout of the radius server.
        type: int
      retransmit:
        description:
          - Specifies the re-transmit value of the radius server.
        type: int
      servers:
        description:
          - Specifies the servers list of the radius server.
        type: dict
        suboptions:
          host:
            description:
              - Specifies the host details of the radius servers list.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                  - Specifies the name of the radius server host.
                type: str
              auth_type:
                description:
                  - Specifies the authentication type of the radius server host.
                type: str
                choices:
                  - pap
                  - chap
                  - mschapv2
              key:
                description:
                  - Specifies the key of the radius server host.
                type: str
              priority:
                description:
                  - Specifies the priority of the radius server host.
                type: int
              port:
                description:
                  - Specifies the port of the radius server host.
                type: int
              timeout:
                description:
                  - Specifies the timeout of the radius server host.
                type: int
              retransmit:
                description:
                  - Specifies the retransmit of the radius server host.
                type: int
              source_interface:
                description:
                  - Specifies the source interface of the radius server host.
                type: str
              vrf:
                description:
                  - Specifies the vrf of the radius server host.
                type: str
  state:
    description:
      - Specifies the operation to be performed on the radius server configured on the device.
      - In case of merged, the input mode configuration will be merged with the existing radius server configuration on the device.
      - In case of deleted the existing radius server mode configuration will be removed from the device.
    default: merged
    choices: ['merged', 'deleted']
    type: str
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#nas-ip-addr: 1.2.3.4
#statistics : True
#timeout    : 10
#auth-type  : chap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#localhost       mschapv2  local     52        2        20      2     mgmt  Ethernet12
#myhost          chap      local     53        3        23      3     mgmt  Ethernet24
#---------------------------------------------------------
#RADIUS Statistics
#---------------------------------------------------------
#
#    - name: Merge radius configurations
#      sonic_radius_server:
#        config:
#          auth_type: chap
#          nas_ip: 1.2.3.4
#          statistics: true
#          timeout: 10
#          servers:
#            host:
#              - name: localhost
#        state: deleted
# After state:
# ------------
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#myhost          chap      local     53        3        23      3     mgmt  Ethernet24


# Using deleted
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#nas-ip-addr: 1.2.3.4
#statistics : True
#timeout    : 10
#auth-type  : chap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#localhost       mschapv2  local     52        2        20      2     mgmt  Ethernet12
#myhost          chap      local     53        3        23      3     mgmt  Ethernet24
#---------------------------------------------------------
#RADIUS Statistics
#---------------------------------------------------------
#
#    - name: Merge radius configurations
#      sonic_radius_server:
#        config:
#        state: deleted
# After state:
# ------------
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap


# Using merged
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#
#    - name: Merge radius configurations
#      sonic_radius_server:
#        config:
#          auth_type: chap
#          key: chap
#          nas_ip: 1.2.3.4
#          statistics: true
#          timeout: 10
#          retransmit: 3
#          servers:
#            host:
#              - name: localhost
#                auth_type: mschapv2
#                key: local
#                priority: 2
#                port: 52
#                retransmit: 2
#                timeout: 20
#                source_interface: Eth 12
#                vrf: mgmt
#        state: merged
# After state:
# ------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#nas-ip-addr: 1.2.3.4
#statistics : True
#timeout    : 10
#auth-type  : chap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#localhost       mschapv2  local     52        2        20      2     mgmt  Ethernet12
#---------------------------------------------------------
#RADIUS Statistics
#---------------------------------------------------------


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.radius_server.radius_server import Radius_serverArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.radius_server.radius_server import Radius_server


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Radius_serverArgs.argument_spec,
                           supports_check_mode=True)

    result = Radius_server(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
