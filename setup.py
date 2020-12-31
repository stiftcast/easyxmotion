#!/usr/bin/env python3

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
    
setup(
    name="easyxmotion",
    url="https://github.com/stiftcast/easyxmotion",
    author="stiftcast",
    author_email="stiftcast@gmail.com",
    version="1.0",
    license="GPLv2",
    description="Jump to windows in a style similar to the easymotion vim plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["easyxmotion"],
    install_requires=[
    # Un-official py3 port of pyosd, the original project and documentation are seemingly unavailable.
	"pyosd @ git+https://github.com/dzen/pyosd@master#egg=pyosd",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Topic :: Desktop Environment :: Window Managers"
    ],
    entry_points={
        "console_scripts": [
            "easyxmotion = easyxmotion:main",
        ],
    },
)
