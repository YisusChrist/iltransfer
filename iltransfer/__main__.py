# -*- coding: utf-8 -*-
"""
Main module of the iltransfer package.

This module contains the main function of the package.

Functions:
    main() -> int: Main function.

TODO:
    * Add support for multiple source paths.
"""

from argparse import Namespace

from core_helpers.updates import check_updates
from core_helpers.utils import exit_session
from rich import print
from rich.traceback import install

from .cli import get_parsed_args
from .config import configure_paths
from .consts import (
    DEBUG,
    EXIT_FAILURE,
    EXIT_SUCCESS,
    GITHUB,
    LOG_PATH,
    PROFILE,
    VERSION,
)
from .file_processing import find_and_move_folders
from .logs import logger


def main() -> None:
    """
    Main function
    """
    # Enable rich error formatting in debug mode
    install(show_locals=DEBUG)
    check_updates(GITHUB, VERSION)

    args: Namespace = get_parsed_args()

    logger.info("Start of session")

    src_path, dest_path = configure_paths(args)
    if not src_path.exists():
        logger.error("Source path %s does not exist", src_path)
        exit_session(EXIT_FAILURE, LOG_PATH)

    find_and_move_folders(src_path, dest_path)

    exit_session(EXIT_SUCCESS, LOG_PATH)


if __name__ == "__main__":
    if DEBUG:
        print("[yellow]Debug mode is enabled[/yellow]")
    if PROFILE:
        import cProfile

        print("[yellow]Profiling is enabled[/yellow]")
        cProfile.run("main()")
    else:
        main()
