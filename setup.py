import os
import shutil
import sys
from setuptools import setup, find_packages
import platform

NAME = "pydracogltf"
AUTHOR = "Liang Ding"
EMAIL = "liangding1990@163.com"
URL = "https://github.com/seed93/pydracogltf"
LICENSE = "MIT License"
DESCRIPTION = "wrapper of blender draco gltf lib, used for trimesh gltf io"

try:
    lib_py = os.path.join(NAME, "__init__.py")
    with open(lib_py, "r", encoding="utf8") as f_v:
        v_line = ""
        for line in f_v.readlines():
            if line.startswith("__version__"):
                v_line = line.strip()
                break
        exec(v_line)  # get __version__ from __init__.py
except FileNotFoundError:
    __version__ = "0.0.0"

try:
    with open("README.md", encoding="utf8") as f_r:
        _long_description = f_r.read()
except FileNotFoundError:
    _long_description = ""

if __name__ == "__main__":
    path = {
            'win32': ['libs/extern_draco.dll', 'Windows', 'Microsoft :: Windows'],
            'linux': ['libs/libextern_draco.so', 'Linux', 'POSIX :: Linux'],
            'darwin': ['libs/libextern_draco.dylib', 'Mac OS-X', 'MacOS']
        }.get(sys.platform)
    if sys.platform == 'darwin':
        if platform.machine() == 'x86_64':
            shutil.copy("pydracogltf/libs/x64/libextern_draco.dylib", "pydracogltf/libs/libextern_draco.dylib")
        else:
            shutil.copy("pydracogltf/libs/arm64/libextern_draco.dylib", "pydracogltf/libs/libextern_draco.dylib")
    setup(
        name=NAME,
        version=__version__,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        setup_requires=["setuptools>=18.0", "wheel"],
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=_long_description,
        long_description_content_type="text/markdown",
        package_data={
            "pydracogltf": [path[0]]
        },
        platforms=[path[1]],
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            f"Operating System :: {path[2]}",
        ]
    )
