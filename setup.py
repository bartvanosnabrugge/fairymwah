from setuptools import setup
from setuptools import find_packages

with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
   name='fairymwah',
   version='0.1',
   description='FAIR(y) Model Workflow Assembler for Hydrology',
   license="MIT",
   long_description=long_description,
   author='Bart van Osnabrugge',
   author_email='bartvanosnabrugge@usask.ca',
   url="https://github.com/CH-Earth/comphydShared_summa",
   packages=find_packages()
   #packages=['fairymwah']  #same as name
)