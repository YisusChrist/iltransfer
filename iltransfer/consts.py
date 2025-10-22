"""Constants for the project."""

from pathlib import Path

from core_helpers.xdg_paths import PathType, get_user_path

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

metadata_info = metadata.metadata(__package__ or __name__)
__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata_info["Summary"]
PACKAGE = metadata_info["Name"]
GITHUB = (
    metadata_info["Home-page"] or metadata_info["Project-URL"].split(",")[1].strip()
)
AUTHOR = metadata_info["Author"]

CONFIG_PATH: Path = get_user_path(PACKAGE, PathType.CONFIG)
CONFIG_FILE: Path = CONFIG_PATH / f"{PACKAGE}.ini"
DATA_PATH: Path = get_user_path(PACKAGE, PathType.DATA)
LOG_PATH: Path = get_user_path(PACKAGE, PathType.LOG)
LOG_FILE: Path = LOG_PATH / f"{PACKAGE}.log"

DEFAULT_SRC_PATH: Path = DATA_PATH / "instagram"
DEFAULT_DEST_PATH: Path = DATA_PATH / "move"

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

SLEEP_TIME = 0.5
