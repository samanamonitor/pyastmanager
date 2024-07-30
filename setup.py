from setuptools import setup, find_packages
from astmanager import __version__
import re, os


if __name__ == "__main__":
    setup(
        name='astmanager',
        version=__version__,
        packages=find_packages(include=['astmanager', 'astmanager.*']),
        data_files=[],
        install_requires=[ ]
    )
