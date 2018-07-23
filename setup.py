import os
from setuptools import setup, find_packages


setup(
    name = 'mlb-normalize-player-ids',
    version = '0.1.0',
    description = ("""
        Translates known baseball player id registers
        (Chadwick, Smart Fantasy Baseball, Crunchtime)
        into a unified schema
    """),
    author = 'Matt Dennewitz',
    author_email = 'mattdennewitz@gmail.com',
    url = 'https://github.com/mattdennewitz/mlb-normalize-player-ids',

    install_requires = [
        'click',
        'schematics',
    ],

    packages = find_packages(),

    scripts = [
        'bin/bid-normalize-register'
    ],
)
