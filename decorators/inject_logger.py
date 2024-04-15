import inject
import logging
import functools

def inject_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        return func(*args, logger=logger, **kwargs)
    return wrapper
