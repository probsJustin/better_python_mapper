import logging

def configFile(configFileLocation, logLevel):
    try:
        if(logLevel == "debug"):
            logLevel = logging.DEBUG
        if(logLevel == "info"):
            logLevel = logging.INFO
        logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=configFileLocation, level=logLevel)
    except Exception as error:
        print(f'[ERROR] LOGGER-ERROR {error}')

def debug(msg):
    try:
        print(f'[DEBUG] {msg}')
        logging.debug(msg)
    except Exception as error:
        print(f'[ERROR] LOGGER-ERROR {error}')

def info(msg):
    try:
        print(f'[INFO] {msg}')
        logging.info(msg)
    except Exception as error:
        print(f'[ERROR] LOGGER-ERROR {error}')

def error(msg):
    try:
        print(f'[ERROR] {msg}')
        logging.error(msg)
    except Exception as error:
        print(f'[ERROR] LOGGER-ERROR {error}')




