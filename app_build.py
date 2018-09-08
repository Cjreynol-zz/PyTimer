from os                 import path
from setuptools         import setup

from pytimer.__main__   import __version__


APP_NAME = "PyTimer"
APP_MAIN = [path.join("pytimer", "__main__.py")]

VERSION_STRING = '.'.join(__version__)
ICON_FILE = path.join("assets", "pytimer.icns")

DATA_FILES = []

OPTIONS = {
    "iconfile": ICON_FILE,
    "plist": {
        "CFBundleDevelopmentRegion": "en-US",
        "CFBundleDisplayName": APP_NAME,
        "CFBundleIdentifier": "info.chadreynolds.macOS." + APP_NAME,
        "CFBundleName": APP_NAME,
        "CFBundlePackageType": "APPL",
        "CFBundleShortVersionString": VERSION_STRING,
        "CFBundleVersion": VERSION_STRING,
        "NSHumanReadableCopyright": 
                    u"Copyright © 2018, Chad Reynolds, All Rights Reserved",
        "CFBundleDocumentTypes": [
            {
                "CFBundleTypeName": "PyTimer Split File",
                "CFBundleTypeIconFiles": [ICON_FILE],
                "CFBundleTypeExtensions": ["pytimer"],
                "LSHandlerRank": "Owner"
            }
        ]
    }
}

setup(
    name = APP_NAME,
    app = APP_MAIN,
    data_files = DATA_FILES,
    options = {"py2app": OPTIONS},
    setup_requires = ["py2app"],
)
