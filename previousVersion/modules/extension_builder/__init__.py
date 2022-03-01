import json
import previousVersion.modules.extension as extension
import previousVersion.modules.my_logger as my_logger
import traceback

my_logger.config_file("./logs/extension_builder.log", "debug")


def parse(target_file):
    try:
        with open(target_file) as f:
            target_data = json.load(f)
        target_data_list = list()
        for x in target_data:
            my_logger.debug(f'[EXTENSION BUILDER]: Created Target Object for {target_data[x]["FULL_TARGET_URL"]}')
            target_data_list.append(extension.ExtensionInstance(target_data[x]["FULL_TARGET_URL"],
                                                                target_data[x]["FILTERS"], target_data[x]["THREADS"],
                                                                target_data[x]["PRIORITY_LEVEL"]))
        return target_data_list

    except Exception as error:
        my_logger.error(f'[{ __name__ }]: .parse failed, caught exception: "{error}"')
        my_logger.error(f'[{ __name__ }]: .parse failed, caught exception: "{traceback.format_exc()}"')
        return False
