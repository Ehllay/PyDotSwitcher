import os

# Versioning
__version__ = "0.0.1"

# Directories
HOME = os.path.expanduser("~")

CACHE_DIR = f"{HOME}/.cache/pydotswitcher"
GRP_DIR = f"{HOME}/.config/pydotswitcher/groups"

# Backup
BACKUP_DIR = f"{HOME}/.config/pydotswitcher/backups"
MAX_BACKUPS = 3
