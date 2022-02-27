from bs4 import BeautifulSoup as bs
import requests
import json
from os.path import exists
import modules.myLogger as myLogger
'''
url = 'http://example.com'
r = requests.get(url)
tree = bs(r.text, 'html.parser') # Parse into tree
for link in tree.find_all('a'): # find all "a" anchor elements.
    print(f"{link.get('href')} -> {link.text}")
'''

def merge(dict1, dict2):
    try:
        myLogger.debug(f'[{__name__}]: Merging old and new stored trees')
        z = dict1.copy()   # start with keys and values of x
        z.update(dict2)    # modifies z with keys and values of y
        return z
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: Note able to merge trees: "{error}"')

def sendRequest(target_url, target_name):
    try:
        myLogger.configFile("./logs/extensionBuilder.log", "debug")
        r = requests.get(target_url)
        tree = bs(r.text, 'html.parser')  # Parse into tree
        requestObj = dict()
        for link in tree.find_all('a'):  # find all "a" anchor elements.
            requestObj[link.get('href')] = 0
        writeToFile(requestObj, target_name)
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: Unable to send request for "{target_url}"')
        myLogger.error(f'[{ __name__ }]: sendRequest caught error: "{error}"')



def checkIfExists(fileName):
    try:
        return exists(fileName)
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: checkIfExists caught error: "{error}"')


def readFromFile(full_directory_path):
    myLogger.debug(f'[{ __name__ }]: Reading previous stored trees "{full_directory_path}"')
    try:
        if(checkIfExists(full_directory_path)):
            with open(full_directory_path, 'r') as f:
                objectFromFile = json.load(f)
            f.close()
            return objectFromFile
        else:
            return False
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: readFromFile caught error: "{error}"')
        return False

def replaceDots(fileName):
    try:
        return fileName.replace('.', '_')
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: replaceDots caught error: "{error}"')


def writeToFile(objectToWrite_new, fileName):
    try:
        fileName = replaceDots(fileName)
        objectToWrite_new_to_write = dict()
        full_directory_path = f'./stored_trees/{fileName}.json'
        objectToWrite_old = readFromFile(full_directory_path)
        if(objectToWrite_old == False or objectToWrite_old == None or objectToWrite_old == "null"):
            objectToWrite_new_to_write = objectToWrite_new
        else:
            objectToWrite_new_to_write = merge(objectToWrite_old, objectToWrite_new)
        myLogger.debug(f'[{ __name__ }]: Writing new stored tree for {fileName}')
        with open(f'./stored_trees/{fileName}.json', 'w', encoding='utf-8') as file:
            json.dump(objectToWrite_new_to_write, file, ensure_ascii=False, indent=4)

        myLogger.debug(f'[{__name__}]: Completed writing to stored tree file: {fileName}')

    except Exception as error:
        myLogger.error(f'[{__name__}]: writeToFile caught error: "{error}"')



