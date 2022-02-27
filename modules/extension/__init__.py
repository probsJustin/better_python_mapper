import re
from urllib.parse import urlparse
import modules.my_logger as my_logger

my_logger.config_file("./logs/creating_new_extension_instance.log", "debug")


class ExtensionInstance:
    #    FILTERS = [".jpg", ".gif", ".png", ".css"]
    FILTERS = []
    NAME = ""
    STORAGE_FILE_DIR = ""
    TARGET = ""
    THREADS = 1
    URL_PARSED_OBJECT = ""
    PRIORITY_LEVEL = 0

    def __init__(self, target_url, filters, threads, priority_level):
        try:
            self.set_target(target_url)
            self.set_name(target_url)
            self.create_storage_file_dir()
            self.set_filters(filters)
            self.create_current_url()
            self.set_threads(threads)
            self.set_priority_level(priority_level)
        except Exception as error:
            my_logger.error(f'[{ __name__ }]: Not able to create new extension instance: "{error}"')

    def __repr__(self):
        try:
            return f'[{self.get_name()}][URL]:{self.get_target()}'
        except Exception as error:
            my_logger.error(f'[{ __name__ }]: Not able to print extension instance: "{error}"')

# BELOW THIS ARE JUST SETTERS, GETTERS AND CREATES FOR DATA FOR THE EXTENSION IT SELF

    def set_priority_level(self, priority_level):
        self.PRIORITY_LEVEL = priority_level

    def get_priority_level(self):
        return self.PRIORITY_LEVEL

    def set_filters(self, filters):
        self.FILTERS = filters

    def set_target(self, targetURL):
        self.TARGET = targetURL

    def get_target(self):
        return self.TARGET

    def create_storage_file_dir(self):
        self.STORAGE_FILE_DIR = f'./stored_trees/{self.NAME}'

    def set_storage_file_dir(self, file_directory):
        self.STORAGE_FILE_DIR = file_directory

    def get_storage_file_dir(self):
        return self.STORAGE_FILE_DIR

    def set_name(self, target_url):
        try:
            self.NAME = re.search("^(?:http.?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)", target_url)[1]
        except Exception as error:
            my_logger.error(f'[{__name__}]: set_name caught error: "{error}"')

    def get_name(self):
        return self.NAME

    def create_current_url(self):
        try:
            self.URL_PARSED_OBJECT = urlparse(self.TARGET)
        except Exception as error:
            my_logger.error(f'[{__name__}]: create_current_url caught error: "{error}"')

    def set_current_url(self):
        try:
            self.URL_PARSED_OBJECT = urlparse(self.TARGET)
        except Exception as error:
            my_logger.error(f'[{__name__}]: create_current_url caught error: "{error}"')

    def get_current_url(self):
        return self.URL_PARSED_OBJECT

    def set_threads(self, threads):
        self.THREADS = threads

    def get_threads(self):
        return self.THREADS
