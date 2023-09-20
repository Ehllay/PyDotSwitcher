# File managment

import os
import sys
import shutil

from .vars import PDS_DIR


def create_dir(dir):
    os.makedirs(dir, exist_ok=True)


def mkgroup(group):
    create_dir(f"{PDS_DIR}/{group}")
    print(f"Created dotfile group {group}")


def copy_to_group(args):
    appends = args[:-1]
    group = args[-1]

    group_dir = os.path.join(PDS_DIR, group)
    print(group_dir)

    for file in appends:
        if file[0] == ".":
            pwd = os.getcwd()
            file = os.path.join(pwd, file)

        if not os.path.isdir(group_dir):
            print(f"Group {group} does not exist")
            sys.exit()

        if not os.path.exists(file):
            print(f"File '{file}' does not exist")

        file = os.path.expanduser(file)

        for root, _, files in os.walk(file):
            rel_path = os.path.relpath(root, file)
            group_path = os.path.join(group_dir, rel_path)

            # os.makedirs(group_path, exist_ok=True)

            for subfile in files:
                src_file = os.path.join(root, subfile)
                dest_file = os.path.join(group_path, subfile)

                print(src_file, "->", dest_file)
                try:
                    # shutil.copy2(src_file, dest_file)
                    pass
                except FileExistsError:
                    pass

        print(f"Copied {file} to {group}")
