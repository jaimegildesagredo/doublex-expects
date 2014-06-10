# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def _parse_requirements(path):
    reqs, links = [], []

    for req in open(path):
        req = req.split()

        if req[0] == '-e':
            links.append(req[1])
            reqs.append(_get_req_name(req[1]))
        else:
            reqs.append(req[0])

    return reqs, links


def _get_req_name(value):
    return value.split('#')[1].split('=')[1]


requirements, dependency_links = _parse_requirements('requirements.txt')
long_description = open('README.rst').read()

setup(
    name='doublex-expects',
    version='0.2.0',
    description='Expects plugin for Doublex test doubles assertions',
    long_description=long_description,
    url='https://github.com/jaimegildesagredo/doublex-expects',
    author='Jaime Gil de Sagredo Luna',
    author_email='jaimegildesagredo@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['specs', 'specs.*']),
    install_requires=requirements,
    dependency_links=dependency_links,
    entry_points={
        'expects.type_plugins': [
            'doublex.internal.Method = doublex_expects:Spy'
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
