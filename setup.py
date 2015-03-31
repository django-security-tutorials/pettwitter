from codecs import open
from setuptools import setup
import os

extra_depends = []
if 'DYNO' in os.environ:
    extra_depends.append('dj-database-url==0.3.0')

setup(
    name='thesite',
    version='0.1',
    description='A Django app',
    install_requires=extra_depends,
)
