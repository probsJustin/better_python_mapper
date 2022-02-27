import re
from urllib.parse import urlparse
import modules.my_logger as my_logger
import json

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

    def read_from_stored_trees(self):
        full_directory_path = self.STORAGE_FILE_DIR
        my_logger.debug(f'[{__name__}]: Reading previous stored trees "{full_directory_path}"')
        try:

            with open(full_directory_path, 'r') as f:
                object_from_file = json.load(f)
            f.close()
            return object_from_file
        except Exception as error:
            my_logger.error(f'[{__name__}]: read_from_file caught error: "{error}"')
            return False

    def parse_self_responses(self):
        self.create_new_target_from_self(self.read_from_stored_trees())

    def create_new_target_from_self(self, target_url_list):
        new_target_object_file = dict()
        for x in target_url_list:
            new_target_object_file[x] = dict()
            new_target_object_file[x]["FULL_TARGET_URL"] = x
            new_target_object_file[x]["FILTERS"] = self.FILTERS
            new_target_object_file[x]["THREADS"] = self.get_threads()
            new_target_object_file[x]["PRIORITY_LEVEL"] = self.get_priority_level()


        with open(f'./targets/new_{self.replace_dots(self.NAME)}.json', 'w', encoding='utf-8') as file:
            json.dump(new_target_object_file, file, ensure_ascii=False, indent=4)

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

        self.STORAGE_FILE_DIR = f'./stored_trees/{self.replace_dots(self.NAME)}.json'

    def set_storage_file_dir(self, file_directory):
        self.STORAGE_FILE_DIR = file_directory

    def get_storage_file_dir(self):
        return self.STORAGE_FILE_DIR

    def replace_dots(self, file_name):
        try:
            return file_name.replace('.', '_')
        except Exception as error:
            my_logger.error(f'[{__name__}]: replace_dots caught error: "{error}"')

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
