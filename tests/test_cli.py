from iltransfer.cli import get_parsed_args
from argparse import Namespace


def test_get_parsed_args_with_no_args():
    # Test when no command-line arguments are provided
    args = get_parsed_args()

    # Assert that the returned object is an argparse.Namespace
    assert isinstance(args, Namespace)

    # Add more assertions to check specific properties of the Namespace object
    # TODO: Continue adding more tests
