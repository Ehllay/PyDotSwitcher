# File managment

import os
import sys
import shutil

from .vars import HOME, PDS_DIR


def create_dir(dir):
    os.makedirs(dir, exist_ok=True)


def mkgroup(group):
    create_dir(f"{PDS_DIR}/{group}")
    print(f"Created dotfile group {group}")


def copy_to_group(file, group):
    group_dir = f"{PDS_DIR}/{group}"

    if file[0] == ".":
        pwd = os.getcwd()
        file = os.path.join(pwd, file)

    if not os.path.isdir(group_dir):
        print(f"Group {group} does not exist")
        sys.exit()

    if not os.path.exists(file):
        print("Invalid file")
        sys.exit()

    shutil.copy(file, group_dir)
    print(f"Copied {file} to {group}")
