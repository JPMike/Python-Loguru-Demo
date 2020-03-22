import logging
import sys
from os import makedirs
from os.path import dirname, exists

loggers = {}

LOG_ENABLED = True
LOG_TO_CONSOLE = True
LOG_TO_FILE = True

LOG_PATH = "./logs/standard.log"
LOG_LEVEL = "DEBUG"
LOG_FORMAT = "%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s " \
             "- %(message)s "
LOG_ENVIRONMENT = "dev"


def get_logger(name=None):
    global loggers
    if not name:
        name = __name__

    if loggers.get(name):
        return loggers.get(name)

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if LOG_ENABLED and LOG_TO_CONSOLE:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if LOG_ENABLED and LOG_TO_FILE:
        log_dir = dirname(LOG_PATH)
        if not exists(log_dir):
            makedirs(log_dir)

        file_handler = logging.FileHandler(LOG_PATH, encoding='utf-8')
        file_handler.setLevel(LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    loggers[name] = logger
    return logger


if __name__ == '__main__':
    standard_logger = get_logger()
    standard_logger.debug("standard logger debug.")
    another_standard_logger = get_logger()
    another_standard_logger.info("another_standard_logger logger info.")
