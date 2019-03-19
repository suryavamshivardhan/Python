import os
import json
import logging
from com.logger import logging_init

def setup(
    default_path='../../resources/config.json',
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
        with open(path, 'rt') as f:
            config = json.load(f)
    else:
        logger.error("Application config file is not available at resources, please check !!")
        raise ValueError("Application config file is not available at resources, please check !!")
    return config


