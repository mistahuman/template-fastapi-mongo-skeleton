import os
from dotenv import load_dotenv
import logging
import logging.config
import yaml


load_dotenv()

class Config:
    version = os.getenv('BACKEND_VERSION')
    title = os.getenv('BACKEND_NAME')

    app_settings = {
        'db_name': os.getenv('MONGO_DB'),
        'mongodb_url': os.getenv('MONGO_URI'),
        'db_username': os.getenv('MONGO_USER'),
        'db_password': os.getenv('MONGO_PASSWORD'),
    }


def setup_advanced_logging(default_path='app/conf/logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
    else:
        print('Failed to load configuration file. Using default configs')
        logging.basicConfig(level=default_level)
