import logging
from datetime import datetime

def configFile(configFileLocation, logLevel):
    try:
        if(logLevel == "debug"):
            logLevel = logging.DEBUG
        if(logLevel == "info"):
            logLevel = logging.INFO
        logging.basicConfig(format='[%(asctime)s]%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=configFileLocation, level=logLevel)
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




