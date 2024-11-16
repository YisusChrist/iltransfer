"""Constants for the project."""

from core_helpers.xdg_paths import get_user_path

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata.metadata(__package__ or __name__)["Summary"]
GITHUB: str = metadata.metadata(__package__ or __name__)["Home-page"]
PACKAGE = metadata.metadata(__package__ or __name__)["Name"]

CONFIG_PATH = get_user_path(PACKAGE, "config")
CONFIG_FILE = CONFIG_PATH / f"{PACKAGE}.ini"
DATA_PATH = get_user_path(PACKAGE, "data")
LOG_PATH = get_user_path(PACKAGE, "log")
LOG_FILE = LOG_PATH / f"{PACKAGE}.log"

VERSION = __version__
DESC = __desc__

DEFAULT_SRC_PATH = DATA_PATH / "instagram"
DEFAULT_DEST_PATH = DATA_PATH / "move"

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False
