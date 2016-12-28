import functools
import logging


def log_result(logger=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.debug('%s(): %s', func.__name__, result)
            return result

        return wrapper

    if not isinstance(logger, logging.Logger):
        func = logger
        logger = logging.getLogger()
        return decorator(func)

    return decorator
