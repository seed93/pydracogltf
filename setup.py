import os
import sys
from setuptools import setup, find_packages
import platform

NAME = "pydracogltf"
AUTHOR = "Liang Ding"
EMAIL = "liangding1990@163.com"
URL = "https://github.com/seed93/pydracogltf"
LICENSE = "MIT"
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
            'win32': 'libs/extern_draco.dll',
            'linux': 'libs/libextern_draco.so',
            'darwin': 'libs/libextern_draco.dylib'
        }.get(sys.platform)
    if sys.platform == 'darwin':
        if platform.machine() == 'x86_64':
            os.copy("pydracogltf/libs/x64/libextern_draco.dylib", "pydracogltf/libs/libextern_draco.dylib")
        else:
            os.copy("pydracogltf/libs/arm64/libextern_draco.dylib", "pydracogltf/libs/libextern_draco.dylib")
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
            "pydracogltf": [path]
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent",
        ]
    )
