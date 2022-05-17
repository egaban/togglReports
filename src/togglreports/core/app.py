from argparse import ArgumentParser
import json

from togglreports import cli_parser, config
from togglreports.core import plugin_loader, report_factory

class Application():
    _parser: ArgumentParser = None

    def run(self):
        # Initialize the application
        self._initialize()

        # Load the plugins
        self._load_plugins()

        # Parse the arguments
        cli_parser.process_arguments(self._parser)



    def _initialize(self):
        # Initialize the configuration if not present
        if not config.config_exists():
            config.init_config()
        
        self._parser = cli_parser.create_parser()
        if not self._parser:
            raise Exception('Parser not initialized')
            exit(1)

    def _load_plugins(self):
        plugin_loader.load_plugins()

