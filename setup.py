from setuptools import setup, find_packages

setup(
    name='ps_utils',
    version='0.1.0',
    description='All general purpose utilities',
    long_description='general purpose utilities',
    author='Phani Sarma',
    author_email='phani.mfe@gmail.com',
    url='https://github.com/phanigenin',
    install_requires=[],
    packages=find_packages(exclude=('docs'))
)