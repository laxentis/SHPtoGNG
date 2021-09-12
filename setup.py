from cx_Freeze import setup, Executable
from setuptools import PackageFinder

base = None

executables = [Executable("GNG.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="SHP to GNG",
    options=options,
    version="1.0",
    description='Converts SHP files to GNG importable data',
    executables=executables
)