import setuptools
from setuptools import setup

setup(
    name='PyThermoML',
    version='1.1.1',
    description='jupyterNotebookTest',
    url = 'https://github.com/undefinedSolutions/jupyterNotebookTest',
    author='Wunderlich, Mike',
    packages=setuptools.find_packages(),
    _install_requires=['python','numpy','matplotlib','pandas','bokeh','rise'],
)