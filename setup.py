from setuptools import setup, find_packages

# Package metadata
NAME = 'dust3r'
VERSION = '1.0.0'
DESCRIPTION = 'zData implementation of Dust3r model'
AUTHOR = 'Enfuse.io'
EMAIL = 'asakhare@zdatainc.com'
URL = 'https://github.com/zdata-inc/dust3r'
LICENSE = 'MIT'
PYTHON_VERSION = '>=3.11.0'

# Required packages
with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = AUTHOR,
    author_email = EMAIL,
    url = URL,
    license = LICENSE,
    python_requires = PYTHON_VERSION,
    packages = find_packages(),
    # install_requires = required_packages,
    classifiers = [
        'Development Status :: 4 - Production/Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent'
    ],
)