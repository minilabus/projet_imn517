import glob
import os
from setuptools import setup

with open('requirements.txt') as f:
    required_dependencies = f.read().splitlines()
    external_dependencies = []
    for dependency in required_dependencies:
        if dependency[0:2] == '-e':
            repo_name = dependency.split('=')[-1]
            repo_url = dependency[3:]
            external_dependencies.append('{} @ {}'.format(repo_name, repo_url))
        else:
            external_dependencies.append(dependency)

SCRIPTS = glob.glob('scripts/*.py')
# Get version and release info, which is all stored in scilpy/version.py
opts = dict(name='encoding',
            maintainer='minilab',
            maintainer_email='',
            description='Project template for IMN517',
            long_description='Project template for Transmission et Codage des Médias Numériques',
            url='',
            download_url='',
            author='Francois Rheault',
            author_email='francois.m.rheault@usherbrooke.ca',
            version='0.1',
            setup_requires=['numpy'],
            install_requires=external_dependencies,
            scripts=SCRIPTS)

setup(**opts)
