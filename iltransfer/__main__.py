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

from core_helpers.logs import logger
from core_helpers.updates import check_updates
from core_helpers.utils import exit_session
from rich.traceback import install

from .cli import get_parsed_args
from .config import configure_paths
from .consts import EXIT_FAILURE, EXIT_SUCCESS, GITHUB, LOG_FILE, LOG_PATH, PACKAGE
from .consts import __version__ as VERSION
from .file_processing import find_and_move_folders


def main() -> None:
    args: Namespace = get_parsed_args()
    install(show_locals=args.debug)
    logger.setup_logger(PACKAGE, LOG_FILE, args.debug, args.verbose)

    if GITHUB:
        check_updates(GITHUB, VERSION)

    logger.info("Start of session")

    src_path, dest_path = configure_paths(args)
    if not src_path.exists():
        logger.error("Source path %s does not exist", src_path)
        exit_session(EXIT_FAILURE, LOG_PATH)

    find_and_move_folders(src_path, dest_path, args.debug)

    exit_session(EXIT_SUCCESS, LOG_PATH)


if __name__ == "__main__":
    main()
