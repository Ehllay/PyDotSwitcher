# File managment

import os
import sys
import pathlib
import shutil

from .vars import PDS_DIR


def create_dir(dir):
    os.makedirs(dir, exist_ok=True)


def mkgroup(group):
    create_dir(f"{PDS_DIR}/{group}")
    print(f"Created dotfile group {group}")


def printgroup(group):
    print(f"{group} group is located at: {PDS_DIR}/{group}")


def gen_path(src, target, index):
    file = os.path.expanduser(src)

    path = pathlib.Path(file)
    root = path.parts.index(os.getenv("USER")) + index

    return pathlib.Path(target).joinpath(*path.parts[root:])


def copy_to_group(args):
    appends = args[:-1]
    group = args[-1]

    group_dir = os.path.join(PDS_DIR, group)

    for file in appends:
        if file[0] == ".":
            print("Only absolute paths allowed (try with '~' or '/home/user')")
            sys.exit()

        if not os.path.isdir(group_dir):
            print(f"Group {group} does not exist")
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
