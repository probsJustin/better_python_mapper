import modules.myLogger as myLogger
import modules.request_mapper as request_mapper
import modules.extensionBuilder as extensionBuilder

myLogger.configFile("./logs/target_processor.log", "debug")

def getNextTargets(targetFile):
    try:
        nextTarget = extensionBuilder.parse(targetFile)
        return nextTarget
    except Exception as error:
        myLogger.error(f'[{__name__}]: target not able target specific url: "{error}"')
        return False


def target(target_list):
    try:
        for x in target_list:
            request_mapper.initParse(x.TARGET, x.NAME)
        #request_mapper.initParse(target_url, target_name)
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: .target not able target specific url: "{error}"')
        myLogger.error(f'[{ __name__ }]: .target not able target specific url: "{error}"')

def run(targetFile):
    try:
        targetList = getNextTargets(targetFile)

        if not (targetList):
            return False
        else:
            response = target(getNextTargets(targetFile))

        myLogger.debug(f'[{ __name__ }]: .run ran and completed')
        return response
    except Exception as error:
        myLogger.error(f'[{ __name__ }]: .run caught exception: "{error}"')
        return False
