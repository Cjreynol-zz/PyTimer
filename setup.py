"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['pytimer.py']
APP_NAME = "PyTimer"
DATA_FILES = []
OPTIONS = {
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleIdentifier': "info.chadreynolds.osx.pytimer",
        'CFBundleVersion': "1.0.1",
        'CFBundleShortVersionString': "1.0.1",
        'NSHumanReadableCopyright': u"Copyright © 2017, Chad Reynolds, All Rights Reserved"
    }
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
