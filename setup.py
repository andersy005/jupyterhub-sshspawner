#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()

setup(
    maintainer='Anderson Banihirwe',
    maintainer_email='',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='SSH Spawner Plugin for JupyterHub',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description_content_type='text/markdown',
    long_description=long_description,
    include_package_data=True,
    keywords='jupyterhub, spawner',
    name='jupyterhub-sshspawner',
    packages=find_packages(),
    entry_points={},
    url='https://github.com/andersy005/jupyterhub-sshspawner',
    project_urls={
        'Documentation': 'https://github.com/andersy005/jupyterhub-sshspawner',
        'Source': 'https://github.com/andersy005/jupyterhub-sshspawner',
        'Tracker': 'https://github.com/andersy005/jupyterhub-sshspawner/issues',
    },
    zip_safe=False,
)
