__author__ = 'tom'
from setuptools import setup, find_packages

# To build for local development use 'python setup.py develop'.
# To upload a version to pypi use 'python setup.py clean sdist upload'.
# Docs are built with 'make html' in the docs directory parallel to this one
setup(
    name='cvzero',
    version='0.0.1',
    description='Simple library to emulate the Pixy hardware using OpenCV',
    classifiers=['Programming Language :: Python :: 3.7'],
    url='https://github.com/OpenPiRobotics/CVzero',
    author='EDIT ME',
    author_email='EDIT ME',
    license='ASL2.0',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    dependency_links=[],
    zip_safe=False)
