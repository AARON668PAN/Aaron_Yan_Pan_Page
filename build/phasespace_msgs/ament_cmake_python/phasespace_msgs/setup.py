from setuptools import find_packages
from setuptools import setup

setup(
    name='phasespace_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('phasespace_msgs', 'phasespace_msgs.*')),
)
