import sys
import subprocess

# Upgrade pip
#subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# Install torch
subprocess.check_call([sys.executable, "-m", "pip", "install", "torch"])


# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the current version
version = {}
with open("geomloss/__version__.py") as fp:
    exec(fp.read(), version)

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="geomloss",
    version=version["__version__"],
    description="Geometric loss functions between point clouds, images and volumes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jean Feydy",
    author_email="jean.feydy@inria.fr",
    python_requires=">=3",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="kernels optimal transport measure loss geometry",
    packages=["geomloss"],
    package_data={"geomloss": []},
    scripts=[],
    url="",
    license="LICENSE.txt",
    install_requires=[
        "numpy",
        "torch",
    ],
    extras_require={
        "full": [
            "pykeops",
        ],
    },
)
