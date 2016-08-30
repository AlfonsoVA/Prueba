import codecs
import re
from os import path
from distutils.core import setup


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path).read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='numbers',
    version=find_version('numbers.py'),
    py_modules=['numbers'],
    author='Alfonso',
    author_email='AlfonsoVA@ciencias.unam.mx',
    url='https://github.com/AlfonsoVA/Prueba.git',
    description='Python Numbers for Humans.',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
