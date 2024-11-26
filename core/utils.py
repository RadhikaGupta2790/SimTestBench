# utils.py

import logging

class Utils:
    @staticmethod
    def parse_config(config_file):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("Utils")
        logger.info("Parsing config file: %s", config_file)
        # TODO: Implement logic to parse configuration file
        pass
