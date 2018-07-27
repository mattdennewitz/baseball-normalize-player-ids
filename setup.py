"""
Install this application
"""

from setuptools import setup


setup(
    name='baseball-normalize-player-ids',
    version='2018.7.27',
    description=("""
        Translates known baseball player id registers
        (Chadwick, Smart Fantasy Baseball, Crunchtime)
        into a unified schema
    """),
    author='Matt Dennewitz',
    author_email='mattdennewitz@gmail.com',
    url='https://github.com/mattdennewitz/baseball-normalize-player-ids',

    install_requires=[
        'click',
        'schematics',
    ],

    packages=[
        'normalize_ids',
    ],

    scripts=[
        'bin/bid_normalize_register.py'
    ],
)
