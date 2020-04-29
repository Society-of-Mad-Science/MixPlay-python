import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 5):
    raise Exception("mixplay-python makes use of asyncio, async, and"
                    "await, and therefore requires Python >= 3.5.x")

setup(
    name='mixplay-python',
    version='0.1.0',
    description='Reference API implementation for MixPlay',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries'
    ],
    author='AmazingDrMarz',
    author_email='drmarz@manonthemoonstudio.com',
    url='https://github.com/Society-of-Mad-Science/MixPlay-python',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['websockets>=3.3', 'varint>=1.0.2', 'pyee>=3.0.3',
                      'aiohttp>=2.0.7'],
    include_package_data=True,
)
