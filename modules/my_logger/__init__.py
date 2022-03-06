import logging
from datetime import datetime


def config_file(config_file_location, log_level):
    try:

        if log_level == "debug":
            log_level = logging.DEBUG

        if log_level == "info":
            log_level = logging.INFO

        if log_level == "error":
            log_level = logging.ERROR

        logging.basicConfig(format='[%(asctime)s]%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=config_file_location, level=log_level)
    except Exception as error:
        print(f'[{datetime.now()}][ERROR] LOGGER-ERROR {error}')


def debug(msg):
    try:
        print(f'[{datetime.now()}][DEBUG]{msg}')
        logging.debug(msg)
    except Exception as error:
        print(f'[{datetime.now()}][ERROR] LOGGER-ERROR {error}')


def info(msg):
    try:
        print(f'[{datetime.now()}][INFO]{msg}')
        logging.info(msg)
    except Exception as error:
        print(f'[{datetime.now()}][ERROR] LOGGER-ERROR {error}')


def error(msg):
    try:
        print(f'[{datetime.now()}][ERROR]{msg}')
        logging.error(msg)
    except Exception as error:
        print(f'[{datetime.now()}][ERROR] LOGGER-ERROR {error}')




