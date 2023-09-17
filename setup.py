try:
    import pydotswitcher
except ImportError:
    print("PDS requires python 3.11 or greater.")

VERSION = pydotswitcher.__version__
print(VERSION)
