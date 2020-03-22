import sys
import os
from loguru import logger

test_data = {
    "key1": {
        "x": 1,
        "y": 2
    },
    "key2": [3, 4]
}

LOG_PATH = os.path.join(os.path.abspath(os.path.dirname(__name__)), "logs")


def get_log_file(name):
    return os.path.join(LOG_PATH, "{}.log".format(name))


def debug_test():
    logger.add(get_log_file("debug"))
    logger.debug("debug info.")
    logger.debug("debug info: {}", test_data)


def add_func_test():
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.info("here you are.")


def rotation_by_size_test():
    logger.add(get_log_file("rotation_by_size"), rotation="30 KB")
    for num in range(500):
        logger.debug("{num} log to file.".format(num=num))


def rotation_by_time_test():
    logger.add(get_log_file("rotation_by_time"), rotation="12:00")
    for num in range(100):
        logger.debug("{num} log to file.".format(num=num))


def rotation_by_age_test():
    logger.add(get_log_file("rotation_by_age"), rotation="1 week")
    for num in range(100):
        logger.debug("{num} log to file.".format(num=num))


def retention_test():
    logger.add(get_log_file("retention"), retention="10 days")
    for num in range(100):
        logger.debug("{num} log to file.".format(num=num))


def compression_test():
    logger.add(get_log_file("compression"), compression="zip")
    for num in range(1000):
        logger.debug("{num} log to file.".format(num=num))


def log_format_test():
    logger.info("Python Version {}, {feature} coming soon.", sys.version.split(" ")[0], feature="X feature")


class MyException(Exception):
    pass


def exception_catch_test():
    logger.add(get_log_file("exception"))

    @logger.catch()
    def my_func(x, y, z):
        return 1 / (x + y + z)

    @logger.catch(reraise=True)
    def my_exception(x, y, z):
        raise MyException(x, y, z)

    try:
        my_exception(0, 1, -1)
    except MyException as e:
        print(e.args)

    answer = my_func(0, 1, -1)
    print(answer)


def log_async_test():
    logger.add(get_log_file("async"), enqueue=True)
    logger.info("async info")


def full_descriptive_exception_test():
    logger.add(get_log_file("full_exception"), backtrace=True, diagnose=True)

    def func(a, b):
        return a / b

    def nested(c):
        try:
            func(5, c)
        except ZeroDivisionError:
            logger.exception("What Exception!!!")

    nested(0)


def structured_logging_test():
    logger.add(get_log_file("structured"), serialize=True)
    logger.debug(test_data)


def contextualize_test():
    logger.add(get_log_file("context"), format="{extra[ip]} {extra[user]} {message}", serialize=True)
    logger_ctx = logger.bind(ip="127.0.0.1", user="me")
    logger_ctx.info("Contextualize logger.")
    logger_ctx.bind(user="other").info("inline binding other user.")


if __name__ == '__main__':
    # debug_test()
    # add_func_test()
    # rotation_by_size_test()
    # rotation_by_time_test()
    # rotation_by_age_test()
    # retention_test()
    # compression_test()
    # log_format_test()
    # exception_catch_test()
    # log_async_test()
    # full_descriptive_exception_test()
    # structured_logging_test()
    # contextualize_test()
    pass
