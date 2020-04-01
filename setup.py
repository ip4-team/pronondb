# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
   readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pronondb',
    version='0.1.0',
    description='Simple GUI for pronon database management',
    long_description=readme,
    author='Gabriel Olescki',
    author_email='glescki@gmail.com',
    url='https://github.com/glescki/pronondb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
