# Switch it up!

import datetime
import sys
import os
import shutil
import subprocess

from .vars import HOME, GRP_DIR, BACKUP_DIR, MAX_BACKUPS
from .copy import create_dir


def check_backup_dirs():
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a new backup if a backup with the same number doesn't exist
    backup_dir = f"{BACKUP_DIR}/backup_{time}"
    create_dir(backup_dir)

    # Remove oldest backup if the number of backups exceeds the limit
    backups = os.listdir(BACKUP_DIR)

    if len(backups) > MAX_BACKUPS:
        shutil.rmtree(f"{BACKUP_DIR}/{sorted(backups)[0]}")

    print("Backup created at", backup_dir)
    return backup_dir


def backup(group):
    group_dir = os.path.join(GRP_DIR, group)
    backup_dir = check_backup_dirs()

    for dir, _, files in os.walk(group_dir):
        for file in files:
            src_file = os.path.join(dir, file)
            rel_path = os.path.relpath(src_file, group_dir)
            backup_file = os.path.join(backup_dir, rel_path)  # type: ignore

            home_file = os.path.join(HOME, rel_path)

            if os.path.exists(home_file):
                if os.path.isdir(home_file):
                    shutil.copytree(home_file, backup_file, dirs_exist_ok=True)
                else:
                    create_dir(os.path.dirname(backup_file))
                    shutil.copy2(home_file, backup_file)


def switch(group):
    group_dir = os.path.join(GRP_DIR, group)
    list_grp = os.listdir(group_dir)
    for i in list_grp:
        if i.endswith("script.sh"):
            list_grp.remove(i)

    if len(list_grp) == 0:
        print("No dotfiles to copy, aborting")
        sys.exit()

    print("Time to switch it up!")
    backup(group)

    count = 0

    for dir, _, files in os.walk(group_dir):
        for file in files:
            group_file = os.path.join(dir, file)
            rel_path = os.path.relpath(group_file, group_dir)

            home_file = os.path.join(HOME, rel_path)

            if not group_file.endswith("script.sh"):
                shutil.copy2(group_file, home_file)
                count += 1
            else:
                subprocess.call(["sh", group_file])

    print(f"{count} dotfile(s) switched to {group}!")
