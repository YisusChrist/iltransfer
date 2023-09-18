#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of the iltransfer package.

This module contains the main function of the package, which is executed when
the package is run as a script. It also contains the function to parse
command-line arguments, the function to exit the program, and the function to
extract the header key from the module header.

Attributes:
    parser (argparse.ArgumentParser): The argument parser.
    SLEEP_TIME (float): The time to sleep in debug mode.

Functions:
    extract_header_key(key: str) -> str:
        Extract the value associated with the given key from the header.
    get_parsed_args() -> argparse.Namespace:
        Parse and return command-line arguments.
    exit_session(exit_value: int) -> None:
        Exit the program with the given exit value.
    process_folder(folder: Path, dest_path: Path) -> None:
        Processes a folder, checks if it should be skipped, and moves it to the
        destination path if necessary.
    find_and_move_folders(src_path: Path, dest_path: Path) -> None:
        Recursively searches for folders in the source path and moves them to
        the destination path.
    main() -> int:
        Main function.


Example:
    $ python -m iltransfer
"""
import argparse
import shutil
import sys

from pathlib import Path
from rich import print
from rich.traceback import install
from rich_argparse_plus import RichHelpFormatterPlus
from string_grab import grab
from tqdm import tqdm

from .consts import *
from .logs import logger


parser = None
if DEBUG:
    from time import sleep

    SLEEP_TIME = 0.5


def extract_header_key(key: str) -> str:
    """
    Extract the value associated with the given key from the header.

    Args:
        key (str): The key to extract from the header.

    Returns:
        str: The value associated with the key.

    Raises:
        KeyError: If the key is not found in the header.
    """
    try:
        # Open the file and read its contents.
        with open(__file__) as f:
            content = f.read()
        # Extract the value associated with the key.
        return str(grab(content, start=f"@{key}", end="\n").strip())
    except LookupError:
        print(f"[red]Could not extract key '{key}' from header[/red]")
        exit_session(EXIT_FAILURE)


def get_parsed_args() -> argparse.Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as an argparse.Namespace object.
    """
    global parser

    RichHelpFormatterPlus.choose_theme("grey_area")

    parser = argparse.ArgumentParser(
        description=DESC,  # Program description
        formatter_class=RichHelpFormatterPlus,  # Disable line wrapping
        allow_abbrev=False,  # Disable abbreviations
        add_help=False,  # Disable default help
    )

    g_misc = parser.add_argument_group("Miscellaneous Options")
    # Help
    g_misc.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit."
    )
    # Verbose
    g_misc.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show log messages on screen. Default is False.",
    )
    # Debug
    g_misc.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Activate debug logs. Default is False.",
    )
    g_misc.add_argument(
        "-V",
        "--version",
        action="version",
        help="Show version number and exit.",
        version=f"[argparse.prog]{NAME}[/] version [i]{VERSION}[/]",
    )

    return parser.parse_args()


def exit_session(exit_value: int) -> None:
    """
    Exit the program with the given exit value.

    Args:
        exit_value (int): The POSIX exit value to exit with.
    """
    logger.info("End of session")
    # Check if the exit_value is a valid POSIX exit value
    if not 0 <= exit_value <= 255:
        exit_value = EXIT_FAILURE

    if exit_value == EXIT_FAILURE:
        print(
            "[red]There were errors during the execution of the script. "
            f"Check the logs at {LOG_PATH} for more information.[/red]"
        )

    # Exit the program with the given exit value
    sys.exit(exit_value)


def process_folder(folder: Path, dest_path: Path) -> None:
    """
    Processes a folder, checks if it should be skipped, and moves it to the
    destination path if necessary.

    Args:
        folder (Path): The folder to process.
        dest_path (Path): The destination path to move folders to.
    """
    logger.debug(f"Found file {folder}")

    if DEBUG:        
        sleep(SLEEP_TIME)

    if not folder.is_dir():
        logger.warning(f"File {folder} is not a directory. Skipping...")
        return

    subfiles = list(folder.iterdir())
    if len(subfiles) == 1 and subfiles[0].name == "id":
        logger.warning(f"Folder {folder} only contains id file. Skipping...")
        return

    dst_dir = dest_path
    try:
        shutil.move(folder, dst_dir)
        logger.info(f"Moved folder {folder} to {dst_dir}")
    except shutil.Error as e:
        logger.error(e)


def find_and_move_folders(src_path: Path, dest_path: Path) -> None:
    """
    Recursively searches for folders in the source path and moves them to the
    destination path.

    Args:
        src_path (Path): The source path to search for folders.
        dest_path (Path): The destination path to move folders to.
    """
    try:
        file_list = list(src_path.iterdir())
        length = len(file_list)
        logger.info(f"Found {length} files in {src_path}")

        for file in tqdm(iterable=file_list, total=length):
            process_folder(file, dest_path)

    except KeyboardInterrupt:
        print("\nCaught KeyboardInterrupt, terminating workers")


def main() -> int:
    """
    Main function
    """
    args = get_parsed_args()

    logger.info("Start of session")

    # TODO: Use user_config_dir to store the source and destination paths in a config file
    # TODO: Add option to specify source and destination paths

    src_path = Path("D:\\3D Objects\\instagram").resolve()
    dest_path = Path("D:\\3D Objects\\move").resolve()

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
