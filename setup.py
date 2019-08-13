__author__ = 'tom'
from setuptools import setup

required_packages = ['']
extras_rel = ['bump2version', 'twine']
extras_doc = ['sphinx', 'sphinx_rtd_theme']
extras_test = ['nose', 'coverage', 'pycodestyle']
extras_dev = extras_rel + extras_doc + extras_test


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
    packages=['App', 'Library'],
    install_requires=required_packages,
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev]
    extras_require={
        'rel': extras_rel,
        'docs': extras_doc,
        'test': extras_test,
        'dev': extras_dev,
    },
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=extras_test,
    dependency_links=[],
    zip_safe=False)
