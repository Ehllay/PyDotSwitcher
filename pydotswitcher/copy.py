# File managment

import os
import sys
import pathlib
import shutil

from .vars import GRP_DIR


def create_dir(dir):
    os.makedirs(dir, exist_ok=True)


def mkgroup(group):
    create_dir(f"{GRP_DIR}/{group}")
    print(f"Created dotfile group {group}")


def check_group(group):
    group_dir = os.path.join(GRP_DIR, group)

    if not os.path.isdir(group_dir):
        confirmation = input("Group does not exist! Create it? (y/N): ")
        if confirmation.lower() == "y" or "yes":
            mkgroup(group)
        else:
            sys.exit()

    return group_dir


def printgroup(group):
    group_dir = check_group(group)

    print(f"{group} group is located at: {group_dir}")


def gen_path(src, target, index):
    file = os.path.expanduser(src)

    path = pathlib.Path(file)
    root = path.parts.index(os.getenv("USER")) + index

    return pathlib.Path(target).joinpath(*path.parts[root:])


def copy_to_group(args):
    appends = args[:-1]
    group = args[-1]

    group_dir = check_group(group)

    for file in appends:
        if file[0] == ".":
            print("Only absolute paths allowed (try with '~' or '/home/user')")
            sys.exit()

        if not os.path.exists(file):
            print(f"File '{file}' does not exist")

        else:
            copy_path = gen_path(file, group_dir, 1)

            try:
                if os.path.isdir(file):
                    shutil.copytree(file, copy_path)
                else:
                    create_dir(os.path.dirname(copy_path))
                    shutil.copy(file, copy_path)
            except FileExistsError:
                print(f"'{file}' already exists in group, skipping")
            else:
                print(f"Copied {file} to {group}")


def mkscript(group):
    group_dir = check_group(group)

    # Script template
    script = """#!/bin/bash

# Your commands go here

# Example:
# echo "Hi"
"""

    script_path = os.path.join(group_dir, "script.sh")

    if os.path.exists(script_path):
        print("Script already exists, exiting")
        sys.exit()

    with open(script_path, "w") as script_file:
        script_file.write(script)

    print(f"Script created at {script_path}")
