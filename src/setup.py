from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name='CPU bound calculation function',
    ext_modules=cythonize('cy_funcs.pyx')
)
