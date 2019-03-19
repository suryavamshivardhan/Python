import os
import configparser
import logging
from com.logger import logging_init

def setup(
    default_path='../../resources/config.ini',
    env_key='APP_CFG'
):
    """Setup application configuration"""
    logging_init.setup()
    logger=logging.getLogger("com.config.config_reader")
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        config = configparser.ConfigParser()
        config.read(path)
    else:
        logger.error("Application config file is not available at resources, please check !!")
        raise ValueError("Application config file is not available at resources, please check !!")
    return config


