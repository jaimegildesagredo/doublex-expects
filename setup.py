# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()
long_description = open('README.rst').read()

setup(
    name='doublex-expects',
    version='0.1.0',
    description='Expects plugin for Doublex test doubles assertions',
    long_description=long_description,
    url='https://github.com/jaimegildesagredo/doublex-expects',
    author='Jaime Gil de Sagredo Luna',
    author_email='jaimegildesagredo@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['specs', 'specs.*']),
    install_requires=requirements,
    entry_points={
        'expects.plugins': [
            'func = doublex_expects:Spy'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License'
    ]
)
