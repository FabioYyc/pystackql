# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pystackql',
    version='1.0.0',
    description='A Python interface for StackQL',
    long_description=readme,
    author='Jeffrey Aven',
    author_email='javen@stackql.io',
    url='https://github.com/stackql/pystackql',
    license=license,
    packages=['pystackql'],
    # include_package_data=True,
    install_requires=[
        'requests', 
        ],
    # entry_points={
    #     'console_scripts': [
    #         'stackql = pystackql:setup'
    #     ]
    # },
    # classifiers=[
    #     'Operating System :: Microsoft :: Windows',
    #     'Operating System :: MacOS',
    #     'Operating System :: POSIX :: Linux',
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    # ]
)