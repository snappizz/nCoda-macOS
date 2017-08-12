"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['nCoda.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'includes': ['fujian', 'abjad', 'lychee'],
    # 'packages': ['fujian', 'abjad', 'lychee'],
    }

setup(
    app=APP,
    data_files=['programs'],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
