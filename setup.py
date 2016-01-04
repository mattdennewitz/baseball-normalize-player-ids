#!/usr/bin/env python

import os
from setuptools import setup, find_packages

import pip.download
from pip.req import parse_requirements


reqs_txt = os.path.join(os.path.dirname(__file__), 'requirements.txt')
pip_reqs = parse_requirements(reqs_txt, session=pip.download.PipSession())
pip_reqs = [unicode(obj.req) for obj in pip_reqs]

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

    install_requires = pip_reqs,

    packages = find_packages(),

    scripts = [
        'scripts/bid-normalize-register'
    ],
)
