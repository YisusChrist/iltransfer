#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of the iltransfer package.

This module contains the main function of the package.

Functions:
    main() -> int: Main function.

TODO:
    * Add support for multiple source paths.
"""

from rich import print
from rich.traceback import install

from .cli import exit_session, get_parsed_args
from .config import configure_paths
from .consts import *
from .file_processing import find_and_move_folders
from .logs import logger


def main() -> int:
    """
    Main function
    """
    args = get_parsed_args()

    logger.info("Start of session")

    src_path, dest_path = configure_paths(args)
    print(f"[yellow]Source path:[/] {src_path}")
    print(f"[yellow]Destination path:[/] {dest_path}")
    input("Press Enter to continue...")

    if not src_path.exists():
        logger.error(f"Source path {src_path} does not exist")
        exit_session(EXIT_FAILURE)

    find_and_move_folders(src_path, dest_path)

    exit_session(EXIT_SUCCESS)


if __name__ == "__main__":
    # Enable rich error formatting in debug mode
    install(show_locals=DEBUG)
    if DEBUG:
        print("[yellow]Debug mode is enabled[/yellow]")
    if PROFILE:
        import cProfile

        print("[yellow]Profiling is enabled[/yellow]")
        cProfile.run("main()")
    else:
        main()
