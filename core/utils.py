# utils.py

import os
import logging
import yaml

def setup_logging(config_file: str) -> None:
    """
    Sets up the logging configuration from a YAML file.

    :param config_file: Path to the configuration file for logging.
    """
    # Get the absolute path of the config file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Two levels up to reach the project root
    config_file_path = os.path.join(base_dir, config_file)

    with open(config_file_path, 'r') as f:
        config = yaml.safe_load(f)

    # Check if logging configuration is present
    if 'logging' in config:
        logging.basicConfig(
            filename=config['logging']['file'],
            level=config['logging']['level'],
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    else:
        logging.basicConfig(level=logging.INFO)  # Default logging configuration

def load_config(config_file: str) -> dict:
    # Get the absolute path of the config file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Two levels up to reach the project root
    config_file_path = os.path.join(base_dir, config_file)

    with open(config_file_path, 'r') as file:
        return yaml.safe_load(file)