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


def move_folder(src: str | Path, dest: str | Path):
    src_path = Path(src).resolve()
    dest_path = Path(dest).resolve() / src_path.name

    # Check if the destination folder exists
    if not dest_path.exists():
        # If the destination folder does not exist, move the entire source folder
        shutil.move(str(src_path), str(dest_path))
    else:
        # If the destination folder exists, move the contents of the source folder
        for item in src_path.iterdir():
            s: Path = item
            d: Path = dest_path / item.name
            if s.is_dir():
                # If the item is a directory, move it recursively
                if d.exists():
                    move_folder(s, d.parent)  # Recursively merge directories
                else:
                    shutil.move(str(s), str(d))
            else:
                # If the item is a file, move it
                # if d.exists() and d.is_file():
                #    d.unlink()  # Remove the file if it already exists
                shutil.move(str(s), str(d))
        # Optionally, remove the source directory if it's empty
        if not any(src_path.iterdir()):
            src_path.rmdir()


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
        handle_id_file(folder, dest_path)
        return

    if not any(subfile.name == "id" for subfile in subfiles):
        logger.warning("Folder %s doesn't contain an id file. Skipping...", folder)
        # TODO: Try to retrieve the id file and move the folder
        return

    try:
        move_folder(folder, dest_path)
        logger.info("Moved folder %s to %s", folder, dest_path)
    except shutil.Error as error:
        logger.error(error)


def handle_id_file(folder: Path, dest_path: Path) -> None:
    """
    Check if the destination path already contains the id file and verify if
    the file contents are the same. If they are, remove it.

    Args:
        folder (Path): The folder containing the id file.
        dest_path (Path): The destination path to move the folder to.
    """
    id_file: Path = folder / "id"
    if not id_file.exists():
        logger.error("Id file %s doesn't exist", id_file)
        return

    id_content: str = id_file.read_text()

    # Get the folder name
    folder_name: str = folder.name

    # Check if the destination path already contains the id file
    dest_folder: Path = dest_path / folder_name
    if not dest_folder.exists():
        logger.warning(
            "Destination path %s doesn't contain folder %s", dest_path, folder_name
        )
        return
    dest_id_file: Path = dest_folder / id_file.name
    if not dest_id_file.exists():
        logger.warning("Destination path %s doesn't contain id file", dest_folder)
        folder_name = find_folder(dest_path, id_content)
        if not folder_name:
            return

    dest_id_content: str = dest_id_file.read_text()
    if id_content == dest_id_content:
        logger.info("Id file contents are the same. Removing id file %s", id_file)
        id_file.unlink()
        # Optionally, remove the source directory if it's empty
        if not any(folder.iterdir()):
            folder.rmdir()
    else:
        logger.warning("Id file contents are different. Skipping...")


def find_folder(dest_path: Path, id_content: str) -> str:
    """
    Search for a folder in the destination path that contains the id content.

    Args:
        dest_path (Path): The destination path to search for the folder.
        id_content (str): The content of the id file.
    """
    logger.debug("Searching for folder in %s with id content %s", dest_path, id_content)

    for folder in dest_path.iterdir():
        id_file: Path = folder / "id"
        if not id_file.exists():
            logger.warning("Folder %s doesn't contain id file", folder)
            continue

        if id_file.read_text() == id_content:
            logger.info("Found folder %s with id content %s", folder, id_content)
            print(f"Found folder {folder} with id content {id_content}")
            return folder.name

    logger.warning("No folder found with id content %s", id_content)
    print(f"[red]No folder found with id content {id_content}")
    return ""
