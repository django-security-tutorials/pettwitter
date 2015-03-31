from codecs import open
from setuptools import setup
import os

# Note to security researchers -- this trickery here is really
# not part of a security vulnerability. It's just the app maintainers
# trying to have different dependencies on Heroku.
extra_depends = []
if 'DYNO' in os.environ:
    extra_depends.append('dj-database-url==0.3.0')
# end dependency trickery.

setup(
    name='thesite',
    version='0.1',
    description='A Django app',
    install_requires=extra_depends,
)
