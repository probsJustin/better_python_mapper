import json
import modules.extension as extension
import modules.myLogger as myLogger

myLogger.configFile("./logs/extensionBuilder.log", "debug")

def parse(targetFile):
    try:
        with open(targetFile) as f:
            targetData = json.load(f)
        targetDataList = list()
        for x in targetData:
            myLogger.debug(f'[EXTENSION BUILDER]: Created Target Object for {targetData[x]["FULL_TARGET_URL"]}')
            targetDataList.append(extension.ExtensionInstance(targetData[x]["FULL_TARGET_URL"],
                                                      targetData[x]["FILTERS"], targetData[x]["THREADS"],
                                                      targetData[x]["PRIORITY_LEVEL"]))
        return targetDataList
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: .parse failed, caught exception: "{error}"')
        return False
