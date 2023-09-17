# File managment

import os

from .vars import PDS_DIR


def create_dir(dir):
    os.makedirs(dir, exist_ok=True)


def mkgroup(group):
    create_dir(f"{PDS_DIR}/{group}")
    print(f"Created dotfile group {group}")


def copy_to_group(file, group):
    print(f"Copied {file} to {group}")
