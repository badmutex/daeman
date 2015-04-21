from setuptools import setup, find_packages

import os.path

# IMPORTANT: use semantic versioning
# http://semver.org
VERSION = '0.1.0'

NAME = 'daeman'

# ########################################################### version
module_dir = NAME
version_file = os.path.join(module_dir, 'version.py')
version_module_contents = """\
# WARNING
# This file is automatically generated by setup.py
# Do not modify by hand.

version = '{}'
""".format(VERSION)

with open(version_file, 'w') as fd:
    fd.write(version_module_contents)


# ########################################################### setup
setup(name=NAME,
      version=VERSION,
      description='Daemon Manager for Unix systems',
      author="Badi' Abdul-Wahid",
      author_email='abdulwahidc@gmail.com',
      packages=find_packages(),
      )
