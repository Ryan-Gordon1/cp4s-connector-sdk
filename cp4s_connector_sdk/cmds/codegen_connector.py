#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved. MIT
import logging
import os
from resilient import ensure_unicode
# Resilient SDK imports to reuse code and achieve a consistency across the SDKs
from resilient_sdk.cmds.base_cmd import BaseCmd
from resilient_sdk.cmds.codegen import CmdCodegen
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util.sdk_exception import SDKException

LOG = logging.getLogger(__name__)
DEFAULT_CONNECTOR = "CAR"


class ConnectorCodegenCmd(BaseCmd):
    """
    A Class which can be used to generate
    a starter package for a connector.
    """

    CMD_NAME = "codegen"
    CMD_HELP = "Generate boilerplate code to start developing a connector"
    CMD_USAGE = """
    $ cp4s-connector-sdk codegen -p <package_name>
    $ cp4s-connector-sdk codegen -p <package_name> -t CAR
    $ cp4s-connector-sdk codegen -p <package_name> --connectortype UDI
    """
    CMD_ADD_PARSERS = ["io_parser"]

    def setup(self):
        # Define codegen usage and description
        self.parser.usage = self.CMD_USAGE
        self.parser.description = self.CMD_DESCRIPTION

        # Add any positional or optional arguments here
        self.parser.add_argument("-p", "--package",
                                 type=ensure_unicode,
                                 help="(required) Name of new or path to existing package")

        self.parser.add_argument("-t", "--connectortype",
                                 default=DEFAULT_CONNECTOR,
                                 help="(optional) What type of connector you want to generate (CAR, UDI); defaults to CAR")

    