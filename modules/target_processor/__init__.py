import modules.my_logger as my_logger
import modules.request_mapper as request_mapper
import modules.extension_builder as extension_builder

my_logger.config_file("./logs/target_processor.log", "debug")


def get_next_targets(target_file):
    try:
        next_target = extension_builder.parse(target_file)
        return next_target
    except Exception as error:
        my_logger.error(f'[{__name__}]: target not able target specific url: "{error}"')
        return False


def target(target_list):
    try:
        for x in target_list:
            request_mapper.init_parse(x.TARGET, x.NAME)
        #request_mapper.init_parse(target_url, target_name)
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: .target not able target specific url: "{error}"')
        my_logger.error(f'[{ __name__ }]: .target not able target specific url: "{error}"')


def run(target_file):
    try:
        target_list = get_next_targets(target_file)

        if not (target_list):
            return False
        else:
            response = target(target_list)

        my_logger.debug(f'[{ __name__ }]: .run ran and completed')
        return response
    except Exception as error:
        my_logger.error(f'[{ __name__ }]: .run caught exception: "{error}"')
        return False
