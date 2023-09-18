#    ___       ___       __  ____       _ __      __
#   / _ \__ __/ _ \___  / /_/ __/    __(_) /_____/ /  ___ ____
#  / ___/ // / // / _ \/ __/\ \| |/|/ / / __/ __/ _ \/ -_) __/
# /_/   \_, /____/\___/\__/___/|__,__/_/\__/\__/_//_/\__/_/
#      /___/

import argparse
import sys
import os

from .vars import __version__
from . import copy


def main():
    parser = get_args()
    parse(parser)


def get_args():
    # Get flags
    desc = "Switch up your dotfiles!"

    parser = argparse.ArgumentParser(prog="PyDotSwitcher", description=desc)

    # Declare Flags

    parser.add_argument("-v", action="store_true", help="Show current version")

    parser.add_argument(
        "-n",
        "--new_group",
        type=str,
        # action="store",
        metavar="[group]",
        help="Create a new group",
    )

    parser.add_argument(
        "-a",
        "--append",
        nargs=2,
        type=str,
        metavar="[file/dir], [group]",
        help="Append a file or directory to a group",
    )

    parser.add_argument(
        "-s",
        "--script",
        type=str,
        metavar="[group]",
        help="Add a script to the specified group",
    )

    return parser


def parse(parser):
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()

    if args.v:
        print(f"PyDotSwitcher Version: {__version__}")
        sys.exit()

    if args.new_group:
        copy.mkgroup(args.new_group)

    if args.append:
        copy.copy_to_group(*args.append)


if __name__ == "__main__":
    main()
