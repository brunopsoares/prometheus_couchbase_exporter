from setuptools import setup, find_packages
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prometheus-couchbase-exporter',

    version='1.0.0',

    description='Couchbase query Prometheus exporter',
    long_description=long_description,

    url='https://github.com/brunopsoares/prometheus_couchbase_exporter',

    # Author details
    author='Bruno Soares',
    author_email='bruno.soares@jumia.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='monitoring prometheus exporter',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'requests',
        'prometheus-client',
        'statsmetrics'
    ],

    entry_points={
        'console_scripts': [
            'prometheus-couchbase-exporter=prometheus_couchbase_exporter.__init__:main',
        ],
    },
)
