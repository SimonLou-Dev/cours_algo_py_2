"""Logging utilities: logger factory, call logger decorator, and logger mixin."""

import logging
from functools import wraps
from typing import Callable


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for the given module."""
    return logging.getLogger(name)

def log_calls(func: Callable) -> Callable:
    """Log function calls."""
    logger = get_logger(func.__module__)

    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        logger.info("Calling %s", func.__name__)
        try:
            result = func(*args, **kwargs)
            logger.debug("%s completed", func.__name__)
        except Exception as e:
            logger.exception("%s failed", func.__name__)
            raise
        else:
            return result
    return wrapper

class LoggerMixin:
    """Simple mixin to add logger property to classes."""

    @property
    def logger(self) -> logging.Logger:
        """Provide a logger instance for the current class."""
        if not hasattr(self, "_logger"):
            self._logger = get_logger(self.__class__.__name__)
        return self._logger
