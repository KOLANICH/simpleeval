from distutils.core import setup
__version__ = '0.8'

setup(
    name = 'simpleeval',
    py_modules = ['simpleeval'],
    version = __version__,
    description = 'A simple, safe single expression evaluator library.',
    long_description=open('README.rst','r').read(),
    author = 'Daniel Fairhead',
    author_email = 'danthedeckie@gmail.com',
    url = 'https://github.com/danthedeckie/simpleeval',
    download_url = 'https://github.com/danthedeckie/simpleeval/tarball/' + __version__,
    keywords = ['eval', 'simple', 'expression', 'parse', 'ast'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT',
                   'Programming Language :: Python :: 2.7',
                  ],
    )