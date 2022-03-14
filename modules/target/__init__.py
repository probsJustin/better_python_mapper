import re
from urllib.parse import urlparse
import modules.my_logger as my_logger
import validators
from bs4 import BeautifulSoup as bs
import requests
import json

import contextlib
import os
import queue
import requests
import sys
import threading
import time


my_logger.config_file("./logs/creating_new_extension_instance.log", "debug")



class Target:
    #    FILTERS = [".jpg", ".gif", ".png", ".css"]
    FILTERS = []
    NAME = ""
    STORAGE_FILE_DIR = ""
    TARGET_FILE_DIR = ""
    TARGET = ""
    THREADS = 1
    URL_PARSED_OBJECT = ""
    PRIORITY_LEVEL = 0
    TASK_STATUS = ""
    TASK_STATUS_LIST = ['COMPLETE', 'STARTED', 'STOPPED', 'STUCK', 'WAITING', 'STARTING', 'STOPPING', 'MARKED_FOR_CLEANUP']
    answers = queue.Queue()
    web_paths = queue.Queue()


    def __init__(self, target_object, filters, threads, priority_level):
        try:
            self.set_target(target_object)
            self.set_name(target_object)
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

    def send_request(self, request_url):
        try:
            response = requests.get(request_url)
            tree_response = bs(response.text, 'html.parser')  # Parse into tree
            request_object = dict()
            for link in tree_response.find_all('a'):  # find all "a" anchor elements.
                request_object[link.get('href')] = list([0, response.status_code, 'None', 'None'])
            # you can add more things to find here
            return request_object
        except Exception as error:
            my_logger.error(f'[{__name__}]: Unable to send request for "{request_url}"')
            my_logger.error(f'[{__name__}]: send_request caught error: "{error}"')

    def validate_url(url_to_validate):
        try:
            return validators.url(url_to_validate)
        except Exception as error:
            my_logger.error(f'[{__name__}]: validate_url caught error: "{error}"')
            return False

    def worker_method(self):
        while not self.web_paths.empty():
            path = self.web_paths.get()
            url = self.TARGET
            time.sleep(2)
            r = requests.get(url)
            if r.status_code == 200:
                self.answers.put(url)
                sys.stdout.write('+')
            else:
                sys.stdout.write('x')
            sys.stdout.flush()

    def thread_run(self):
    # this will run its self and then store it in a storeage file
        self.set_task_status("STARTING")

        self.set_task_status("STARTED")

        target_instance_thread = list()
        for i in range(self.THREADS):
            print(f'Spawning thread {i}')
            t = threading.Thread(target=self.worker_method)
            target_instance_thread.append(t)
            t.start()

        for thread in target_instance_thread:
            thread.join()

        self.set_task_status("STOPPING")
        self.set_task_status("STOPPED")
        self.set_task_status("COMPLETE")
        self.set_task_status("MARKED_FOR_CLEANUP")
        return True

    def task_complete(self):
        if self.TASK_STATUS == "COMPLETE":
            my_logger.info(f'[{__name__}]: task is complete, marking for cleanup."')
            return True
        else:
            return False

    def set_task_status(self, status):
        self.TASK_STATUS = status

    def get_task_status(self):
        return self.TASK_STATUS

    def write_target_file(self, target_file, data_to_write):
        with open(target_file, 'w') as file:
            json.dump(data_to_write, file)

    def read_target_file(self, target_file):
        with open(target_file) as file:
            return json.load(file)

    def write_storage_file(self, target_file, data_to_write):
        with open(target_file, 'w') as file:
            json.dump(data_to_write, file)

    def read_storage_file(self, storage_file):
        with open(storage_file) as file:
            return json.load(file)

    def get_target_file_dir(self):
        return self.TARGET_FILE_DIR

    def set_target_file_dir(self, target_file_dir):
        self.TARGET_FILE_DIR = target_file_dir

    def parse_target_object(self):
        return True

    def set_priority_level(self, priority_level):
        self.PRIORITY_LEVEL = priority_level

    def get_priority_level(self):
        return self.PRIORITY_LEVEL

    def set_filters(self, filters):
        self.FILTERS = filters

    def set_target(self, target_object):
        self.TARGET = target_object

    def get_target(self):
        return self.TARGET

    def create_storage_file_dir(self):
        self.STORAGE_FILE_DIR = f'./stored_trees/{self.replace_dots(self.NAME)}.json'

    def set_storage_file_dir(self, file_directory):
        self.STORAGE_FILE_DIR = file_directory

    def get_storage_file_dir(self):
        return self.STORAGE_FILE_DIR

    def set_name(self, target_object):
        try:
            self.NAME = re.search("^(?:http.?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)", target_object)[1]
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
