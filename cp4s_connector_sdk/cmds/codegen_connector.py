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
    $ connector-sdk codegen -p <package_name>
    $ connector-sdk codegen -p <package_name> -t CAR
    $ connector-sdk codegen -p <package_name> --connectortype UDI
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

    def execute_command(self, args):
        LOG.debug("called: ConnectorCodegenCmd.execute_command()")
        LOG.info(args)
        if args.package:
            SDKException.command_ran = "{0} {1}".format(
                self.CMD_NAME, "--package | -p")
            LOG.info("%s %s" %
                     ("Generating a package of type", DEFAULT_CONNECTOR))

            ###
            # Perform checks
            ###
            if os.path.exists(args.package):
                raise SDKException(
                    u"'{0}' already exists. Add --reload flag to regenerate it".format(args.package))

            if not sdk_helpers.is_valid_package_name(args.package):
                raise SDKException(
                    u"'{0}' is not a valid package name".format(args.package))

            ###
            # Gather data needed for generation
            ###
            # The package_name will be specified in the args
            package_name = args.package

            # Get output_base, use args.output if defined, else current directory
            output_base = args.output if args.output else os.curdir
            output_base = os.path.join(
                os.path.abspath(output_base), package_name)

            jinja_data = {
                "package_name": package_name
            }

            # If the output_base directory does not exist, create it
            if not os.path.exists(output_base):
                os.makedirs(output_base)

            from jinja2 import Environment, PackageLoader
            jinja_env = Environment(
                # Loads Jinja Templates in cp4s_connector_sdk/<<relative_path_to_templates>>
                loader=PackageLoader("cp4s_connector_sdk", get_jinja_env_location(
                    connecter_type=args.connectertype)),
                trim_blocks=True,  # First newline after a block is removed
                # Leading spaces and tabs are stripped from the start of a line to a block
                lstrip_blocks=True,
                keep_trailing_newline=True  # Preserve the trailing newline when rendering templates
            )
            # Add custom filters to our jinja_env
            sdk_helpers.add_filters_to_jinja_env(jinja_env)

            # Assign one of the mapping dict function to connector_mapping_collector so that below we call one thing
            # but here we define which thing will be called
            # TODO: Review
            connector_mapping_collector = get_car_connector_mapping_dict
            # Prepare a mapping dict based on type of connector
            # This dict maps our package file structure to  Jinja2 templates
            # TODO: Refactor as there can be a UDI or CAR package_mapping_dict
            package_mapping_dict = connector_mapping_collector(jinja_data)

            ###
            # Generate a connector package using jinja
            ###
            newly_generated_files, skipped_files = CmdCodegen.render_jinja_mapping(
                jinja_mapping_dict=package_mapping_dict,
                jinja_env=jinja_env,
                target_dir=output_base,
                package_dir=output_base)

            ###
            # Report the files that were and were not built
            ###
            if newly_generated_files:
                LOG.debug("Newly generated files:\n\t> %s",
                          "\n\t> ".join(newly_generated_files))

            if skipped_files:
                LOG.debug("Files Skipped:\n\t> %s",
                          "\n\t> ".join(skipped_files))

            LOG.info("%s %s" %
                     ("Codegen run finished for ", package_name))
        else:
            self.parser.print_help()