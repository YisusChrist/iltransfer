"""Configuration module for the project."""
import argparse
import configparser
from pathlib import Path
from typing import Tuple

from rich import print

from .consts import *
from .logs import logger


def create_config_file() -> None:
    """
    Create the configuration file.
    """
    logger.debug(f"Creating configuration file at {CONFIG_FILE}")

    config = configparser.ConfigParser()

    config.add_section("Paths")

    DEFAULT_SRC_PATH = "D:\\3D Objects\\instagram"
    DEFAULT_DEST_PATH = "D:\\3D Objects\\move"

    src_path = input("Enter the source path (default: {}): ".format(DEFAULT_SRC_PATH))
    dest_path = input(
        "Enter the destination path (default: {}): ".format(DEFAULT_DEST_PATH)
    )

    config.set("Paths", "src_path", src_path or DEFAULT_SRC_PATH)
    config.set("Paths", "dest_path", dest_path or DEFAULT_DEST_PATH)

    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)


def configure_paths(args: argparse.Namespace) -> Tuple[Path, Path]:
    """
    Get the source and destination path values from the configuration file or
    the command-line arguments.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.

    Returns:
        Tuple[Path, Path]: The source and destination path values.
    """
    logger.debug("Configuring paths")
    if not CONFIG_FILE.is_file():
        # Configuration file doesn't exist, prompt the user for values and create the file
        # Warn the user that the configuration file doesn't exist
        print(
            "[yellow]Configuration file doesn't exist. "
            f"Creating configuration file at {CONFIG_FILE}[/yellow]"
        )
        create_config_file()

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if args.source_path is None:
        args.source_path = config.get("Paths", "src_path")

    if args.dest_path is None:
        args.dest_path = config.get("Paths", "dest_path")

    src_path = Path(args.source_path).resolve()
    dest_path = Path(args.dest_path).resolve()

    return src_path, dest_path
