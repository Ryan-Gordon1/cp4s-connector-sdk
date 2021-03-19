#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved. MIT

""" TODO: module docstring """

import sys
import logging
from cp4s_connector_sdk.cmds.codegen_connector import ConnectorCodegenCmd
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util.sdk_exception import SDKException
from resilient_sdk.util.sdk_argparse import SDKArgumentParser

# Setup logging
LOG = logging.getLogger("cp4s_connector_sdk_log")
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def get_main_app_parser():
    """
    Creates the main 'entry point' parser for cp4s-connector-sdk.

    :return: Main App Parser
    :rtype: argparse.ArgumentParser
    """
    # Define main parser object
    # We use SDKArgumentParser which overwrites the 'error' method
    parser = SDKArgumentParser(
        prog="connector-sdk",
        description="Python SDK for developing CP4S Connectors",
        epilog="For support, please visit ibm.biz/soarcommunity")

    parser.usage = """
    $ connector-sdk <subcommand> ...
    $ connector-sdk -v <subcommand> ...
    $ connector-sdk -h
    """

    # Add --verbose argument
    parser.add_argument("-v", "--verbose",
                        help="Set the log level to DEBUG",
                        action="store_true")

    return parser


def get_main_app_sub_parser(parent_parser):
    """
    Creates and adds a sub_parser to parent_parser.
    Returns the sub_parser

    :param parent_parser: Parser to add the sub_parser to
    :type parent_parser: argparse.ArgumentParser
    :return: Sub Parser
    :rtype: argparse.ArgumentParser
    """
    # Define sub_parser object, its dest is cmd
    sub_parser = parent_parser.add_subparsers(
        title="subcommands",
        description="one of these subcommands must be provided",
        metavar="",
        dest="cmd"
    )

    return sub_parser

