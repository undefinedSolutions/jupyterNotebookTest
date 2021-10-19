import setuptools
from setuptools import setup

setup(
    name='jupyterNotebookTest',
    version='1.1.1',
    description='testing binder with rise',
    url = 'https://github.com/undefinedSolutions/jupyterNotebookTest',
    author='Wunderlich, Mike',
    packages=setuptools.find_packages(),
    install_requires=['python','numpy','matplotlib','pandas','bokeh','rise'],
)