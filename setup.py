# setup and packaging
import sys
import setuptools

try:
    import pydotswitcher
except ImportError:
    print("PDS requires python 3.11 or greater.")
    sys.exit()

README = open("README.md").read()
VERSION = pydotswitcher.__version__
URL = "https://github.com/Ehllay/PyDotSwitcher"
DOWNLOAD_URL = f"{URL}/archive/PDS_{VERSION}.tar.gz"

setuptools.setup(
    name="pydotswitcher",
    version=VERSION,
    author="Ehllay",
    author_email="",
    description="Switch up your dotfiles",
    long_description_content_type="text/markdown",
    long_description=README,
    keywords="dotfiles, backup, utility config ricing colorscheme linux python",
    license="MIT",
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.11 ",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["dotswitch=pydotswitcher.__main__:main"]},
    python_requires=">3.11",
    # TODO: test_suite="tests",
)
