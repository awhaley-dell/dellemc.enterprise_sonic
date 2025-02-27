#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_stp module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class StpArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_stp module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'mutually_exclusive': [['mstp', 'pvst', 'rapid_pvst']],
            'options': {
                'global': {
                    'options': {
                        'bpdu_filter': {'type': 'bool'},
                        'bridge_priority': {'type': 'int'},
                        'disabled_vlans': {'elements': 'str', 'type': 'list'},
                        'enabled_protocol': {'choices': ['mst', 'pvst', 'rapid_pvst'], 'type': 'str'},
                        'fwd_delay': {'type': 'int'},
                        'hello_time': {'type': 'int'},
                        'loop_guard': {'type': 'bool'},
                        'max_age': {'type': 'int'},
                        'portfast': {'type': 'bool'},
                        'root_guard_timeout': {'type': 'int'}
                    },
                    'type': 'dict'
                },
                'interfaces': {
                    'elements': 'dict',
                    'options': {
                        'bpdu_filter': {'type': 'bool'},
                        'bpdu_guard': {'type': 'bool'},
                        'cost': {'type': 'int'},
                        'edge_port': {'type': 'bool'},
                        'guard': {'choices': ['loop', 'root', 'none'], 'type': 'str'},
                        'intf_name': {'required': True, 'type': 'str'},
                        'link_type': {'choices': ['point-to-point', 'shared'], 'type': 'str'},
                        'port_priority': {'type': 'int'},
                        'portfast': {'type': 'bool'},
                        'shutdown': {'type': 'bool'},
                        'stp_enable': {'type': 'bool'},
                        'uplink_fast': {'type': 'bool'}
                    },
                    'type': 'list'
                },
                'mstp': {
                    'options': {
                        'fwd_delay': {'type': 'int'},
                        'hello_time': {'type': 'int'},
                        'max_age': {'type': 'int'},
                        'max_hop': {'type': 'int'},
                        'mst_instances': {
                            'elements': 'dict',
                            'options': {
                                'bridge_priority': {'type': 'int'},
                                'mst_id': {'required': True, 'type': 'int'},
                                'vlans': {'elements': 'str', 'type': 'list'},
                                'interfaces': {
                                    'elements': 'dict',
                                    'options': {
                                        'cost': {'type': 'int'},
                                        'intf_name': {'required': True, 'type': 'str'},
                                        'port_priority': {'type': 'int'}
                                    },
                                    'type': 'list'
                                }
                            },
                            'type': 'list'
                        },
                        'mst_name': {'type': 'str'},
                        'revision': {'type': 'int'}
                    },
                    'type': 'dict'
                },
                'pvst': {
                    'elements': 'dict',
                    'options': {
                        'bridge_priority': {'type': 'int'},
                        'fwd_delay': {'type': 'int'},
                        'hello_time': {'type': 'int'},
                        'vlan_id': {'required': True, 'type': 'int'},
                        'max_age': {'type': 'int'},
                        'interfaces': {
                            'elements': 'dict',
                            'options': {
                                'cost': {'type': 'int'},
                                'intf_name': {'required': True, 'type': 'str'},
                                'port_priority': {'type': 'int'}
                            },
                            'type': 'list'
                        }
                    },
                    'type': 'list'
                },
                'rapid_pvst': {
                    'elements': 'dict',
                    'options': {
                        'bridge_priority': {'type': 'int'},
                        'fwd_delay': {'type': 'int'},
                        'hello_time': {'type': 'int'},
                        'vlan_id': {'required': True, 'type': 'int'},
                        'max_age': {'type': 'int'},
                        'interfaces': {
                            'elements': 'dict',
                            'options': {
                                'cost': {'type': 'int'},
                                'intf_name': {'required': True, 'type': 'str'},
                                'port_priority': {'type': 'int'}
                            },
                            'type': 'list'
                        }
                    },
                    'type': 'list'
                }
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged', 'type': 'str'
        }
    }  # pylint: disable=C0301
