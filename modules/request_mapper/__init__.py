from bs4 import BeautifulSoup as bs
import requests
import json
from os.path import exists
import modules.my_logger as my_logger
import validators

'''
url = 'http://example.com'
r = requests.get(url)
tree = bs(r.text, 'html.parser') # Parse into tree
for link in tree.find_all('a'): # find all "a" anchor elements.
    print(f"{link.get('href')} -> {link.text}")
'''

my_logger.config_file("./logs/request_mapper.log", "debug")


def validate_url(url_to_validate):
    try:
        return validators.url(url_to_validate)
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: validate_url caught error: "{error}"')
        return False


def merge(dict1, dict2):
    try:
        my_logger.debug(f'[{__name__}]: Merging old and new stored trees')
        z = dict1.copy()   # start with keys and values of x
        z.update(dict2)    # modifies z with keys and values of y
        return z
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: Not able to merge trees: "{error}"')


def send_request(target_url, target_name):
    try:
        r = requests.get(target_url)
        tree = bs(r.text, 'html.parser')  # Parse into tree
        request_object = dict()
        for link in tree.find_all('a'):  # find all "a" anchor elements.
            request_object[link.get('href')] = r.status_code
        write_to_file(request_object, target_name)
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: Unable to send request for "{target_url}"')
        my_logger.error(f'[{ __name__ }]: send_request caught error: "{error}"')


def check_if_exists(file_name):
    try:
        return exists(file_name)
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: check_if_exists caught error: "{error}"')


def read_from_file(full_directory_path):
    my_logger.debug(f'[{ __name__ }]: Reading previous stored trees "{full_directory_path}"')
    try:
        if check_if_exists(full_directory_path):
            with open(full_directory_path, 'r') as f:
                object_from_file = json.load(f)
            f.close()
            return object_from_file
        else:
            return False
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: read_from_file caught error: "{error}"')
        return False


def replace_dots(file_name):
    try:
        return file_name.replace('.', '_')
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: replace_dots caught error: "{error}"')


def write_to_file(object_to_write_new, file_name):
    try:
        file_name = replace_dots(file_name)
        object_to_write = dict()
        full_directory_path = f'./stored_trees/{file_name}.json'
        object_to_write_old = read_from_file(full_directory_path)
        if object_to_write_old == False or object_to_write_old == None or object_to_write_old == "null":
            object_to_write = object_to_write
        else:
            object_to_write = merge(object_to_write_old, object_to_write_new)
        my_logger.debug(f'[{ __name__ }]: Writing new stored tree for {file_name}')
        with open(f'./stored_trees/{file_name}.json', 'w', encoding='utf-8') as file:
            json.dump(object_to_write_new, file, ensure_ascii=False, indent=4)

        my_logger.debug(f'[{__name__}]: Completed writing to stored tree file: {file_name}')

    except Exception as error:
        my_logger.error(f'[{__name__}]: write_to_file caught error: "{error}"')


def init_parse(target_url, target_name):
    if validate_url(target_url):
        return send_request(target_url, target_name)
    else:
        my_logger.debug(f'[{__name__}]: init_parse failed for url: "{target_url}"')
        my_logger.debug(f'[{__name__}]: init_parse failed for target_name: "{target_name}"')
        return False
