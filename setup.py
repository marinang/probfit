from distutils.core import setup, Extension
import distutils.util
import subprocess
import numpy as np
source_suffix = 'pyx'
has_cython = False
try:
    from Cython.Distutils import build_ext
    has_cython = True
except:
    pass

cmdclass={}
if not has_cython:
    source_suffix = 'c'
else:
    cmdclass = {'build_ext':build_ext}


costfunc = Extension('probfit.costfunc',
                    sources = ['probfit/costfunc.'+source_suffix],
                    include_dirs= [np.get_include()],
                    extra_link_args = [])

pdf = Extension('probfit.pdf',
        sources = ['probfit/pdf.'+source_suffix],
        include_dirs= [np.get_include()],
        extra_link_args = [])

libstat = Extension('probfit._libstat',
        sources = ['probfit/_libstat.'+source_suffix],
        include_dirs= [np.get_include()],
        extra_link_args = [])

funcutil = Extension('probfit.funcutil',
        sources = ['probfit/funcutil.'+source_suffix],
        include_dirs= [np.get_include()],
        extra_link_args = [])

functor = Extension('probfit.functor',
        sources = ['probfit/functor.'+source_suffix],
        include_dirs= [np.get_include()],
        extra_link_args = [])

setup (
       cmdclass=cmdclass,
       name = 'probfit',
       version = '1.0.0',
       description = 'Distribution Fitting/Regression Library',
       author='Piti Ongmongkolkul',
       author_email='piti118@gmail.com',
       url='https://github.com/piti118/dist_fit',
       package_dir = {'probfit': 'probfit'},
       packages = ['probfit'],
       ext_modules = [costfunc, pdf, libstat, funcutil, functor],
       requires=['numpy','iminuit']
       )
