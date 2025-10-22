"""Command-line interface for the project."""

from argparse import Namespace

from core_helpers.cli import ArgparseColorThemes, setup_parser

from .consts import PACKAGE
from .consts import __desc__ as DESC
from .consts import __version__ as VERSION


def get_parsed_args() -> Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as an Namespace object.
    """
    parser, g_main = setup_parser(
        PACKAGE,
        DESC,
        VERSION,
        ArgparseColorThemes.GREY_AREA,
    )

    # Source path argument
    g_main.add_argument(
        "-src",
        "--source",
        dest="source_path",
        type=str,
        help="Specify the source path for Instagram profiles.",
    )
    # Destination path argument
    g_main.add_argument(
        "-dst",
        "--destination",
        dest="dest_path",
        type=str,
        help="Specify the destination path for moving profiles.",
    )
    # Config file argument
    g_main.add_argument(
        "-c",
        "--config",
        dest="config_file",
        type=str,
        help="Specify a configuration file.",
    )
    # Create config file interactive
    g_main.add_argument(
        "-i",
        "--interactive",
        dest="interactive",
        action="store_true",
        default=False,
        help="Create a configuration file interactively.",
    )

    return parser.parse_args()
