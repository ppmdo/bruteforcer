from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='bruteforcer',
    version="0.0.1",
    author="Pablo Prieto",
    packages=find_packages(),
    ext_modules=cythonize('bruteforcer/cy_funcs.pyx')
)
