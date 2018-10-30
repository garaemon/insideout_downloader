#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='insideout_downloader',
    version='1.0.0',
    url='https://github.com/garaemon/insideout_downloader.git',
    author='garaemon',
    author_email='garaemon@gmail.com',
    description='Download insideout mp3 file',
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'arrow', 'mutagen'],
    scripts=['bin/insideout_downloader']
)
