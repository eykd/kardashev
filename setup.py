# -*- coding: utf-8 -*-
from setuptools import setup

PROJECT_NAME = 'kardashev'
VERSION = '0.1.dev0'

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = "David Eyk",
    author_email = "david.eyk@gmail.com",
    modules = [PROJECT_NAME],
    install_requires = [
        'arrow==0.10.0',
        'attrs==16.3.0',
        'frozendict==1.2',
        'memoize==1.0.0',
        # 'requests==2.11.1',
        # 'pytz',
        # 'astral==1.3.2',
        'numpy==1.11.1',
        # 'Jinja2==2.8',
        # 'SQLAlchemy==1.0.15',
        # 'click==6.6',
        # 'path.py==8.2.1',
        'pydux==0.2.1',
        'straight.plugin==1.4.1',
        'urwid==1.3.1',
    ],
    entry_points = dict(
        console_scripts = [
            'kardashev = kardashev.cli:main',
        ]
    ),
)
