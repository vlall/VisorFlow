NAME         = 'SoundVolt'
DESCRIPTION  = 'Music stat tools for Python'
AUTHOR       = 'Vishal Lall'
AUTHOR_EMAIL = 'vlall@emory'
URL          = 'http://vishallall.com/soundvolt'
LICENSE      = 'GPLv3'
VERSION      = '0.1'

if __name__ == "__main__":

    from setuptools import setup, Extension, find_packages
    #from distutils.core import setup, Extension
    
    # Setup for BayesPy
    setup(
          install_requires = ['numpy>=1.7.1', # 1.7.0 contains a memory leak bug fixed in 1.7.1
                              'scipy>=0.11.0',
                              #'scikits.sparse>=0.1', # required for sparse GPs only
                              'matplotlib>=1.2.0',
                              'h5py'],
          ## requires = ['numpy (>=1.7.1)', # 1.7.0 contains a memory leak bug
          ##             'scipy (>=0.11.0)',
          ##             'scikits.sparse (>=0.1)',
          ##             'matplotlib (>=1.2.0)',
          ##             'cython',
          ##             'h5py'],

          ## dependency_links = [
          ##     'https://github.com/numpy/numpy/archive/master.zip#egg=numpy-1.8.0',
          ##     ],
              
          # These are for sparse_distance Cython extension
          cmdclass = {'build_ext': build_ext},
          ext_modules = [sparse_distance],
          
          packages = find_packages(),
                      ['SoundVolt',
                       'SoundVolt.demos',
                       'SoundVolt.nodes',
                       'bayespy.plot',
                       'SoundVolt.utils',
                       'SoundVolt.utils.tests',

          name             = NAME,
          version          = VERSION,
          author           = AUTHOR,
          author_email     = AUTHOR_EMAIL,
          description      = DESCRIPTION,
          license          = LICENSE,
          url              = URL,
          long_description = LONG_DESCRIPTION,
          classifiers =
            [ 
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Development Status :: 2 - Pre-Alpha',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Operating System :: OS Independent',
              'Topic :: Scientific/Engineering',
              'Topic :: Scientific/Engineering :: Information Analysis'
            ]
          )

