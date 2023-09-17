"""Logging configuration."""
import logging

from .consts import LOG_FILE, FILE, DEBUG

logger = logging.getLogger(FILE)

handlers = [logging.FileHandler(LOG_FILE)]
level = logging.INFO
msg_format = "[%(asctime)s] %(levelname)s: %(message)s"

if DEBUG:
    level = logging.DEBUG
    msg_format += ": %(pathname)s:%(lineno)d in %(funcName)s"

logging.basicConfig(
    level=level,
    format=msg_format,
    handlers=handlers,
)
