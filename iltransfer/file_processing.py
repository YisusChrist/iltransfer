"""File processing functions."""
import shutil
from pathlib import Path

from rich import print
from tqdm import tqdm

from .consts import DEBUG
from .logs import logger

if DEBUG:
    from time import sleep

    SLEEP_TIME = 0.5


def find_and_move_folders(src_path: Path, dest_path: Path) -> None:
    """
    Recursively searches for folders in the source path and moves them to the
    destination path.

    Args:
        src_path (Path): The source path to search for folders.
        dest_path (Path): The destination path to move folders to.
    """
    logger.debug("Searching for folders in %s", src_path)

    try:
        file_list = list(src_path.iterdir())
        length = len(file_list)
        logger.info("Found %d files in %s", length, src_path)

        for file in tqdm(iterable=file_list, total=length):
            process_folder(file, dest_path)

    except KeyboardInterrupt:
        print("\nCaught KeyboardInterrupt, terminating workers")


def process_folder(folder: Path, dest_path: Path) -> None:
    """
    Processes a folder, checks if it should be skipped, and moves it to the
    destination path if necessary.

    The folder is skipped if it is not a directory or if it only contains an
    id file. When you start downloading a profile, `Instaloader` creates a
    folder with the profile name and an id file inside it. If the download of
    the profile is interrupted while it is fetching the first files, the
    folder will only contain the id file. This is why we check if the folder
    only contains an id file, and if it does, we skip it.

    Args:
        folder (Path): The folder to process.
        dest_path (Path): The destination path to move folders to.
    """
    logger.debug("Processing folder %s", folder)

    if DEBUG:
        sleep(SLEEP_TIME)

    if not folder.is_dir():
        logger.warning("File %s is not a directory. Skipping...", folder)
        return

    subfiles = list(folder.iterdir())
    if len(subfiles) == 1 and subfiles[0].name == "id":
        logger.warning("Folder %s only contains id file. Skipping...", folder)
        return

    if not any(subfile.name == "id" for subfile in subfiles):
        logger.warning("Folder %s doesn't contain an id file. Skipping...", folder)
        return

    try:
        shutil.move(folder, dest_path)
        logger.info("Moved folder %s to %s", folder, dest_path)
    except shutil.Error as error:
        logger.error(error)
