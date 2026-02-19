import yaml
import logging.config

with open("logging.yaml", "r") as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)
