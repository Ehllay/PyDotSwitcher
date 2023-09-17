import os

# Versioning
__version__ = "0.0.1"

# Directories
HOME = os.getenv("HOME", os.getenv("USERPROFILE"))

CACHE_DIR = f"{HOME}/.cache/pydotswitcher"
PDS_DIR = f"{HOME}/.config/pydotswitcher"
