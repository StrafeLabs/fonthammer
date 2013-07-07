import imp
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

version = imp.load_source(
    'fonthammer',
    os.path.join(here, 'fonthammer', '__init__.py')
).__version__

setup(
    name='fonthammer',
    version=version,
    url='http://github.com/StrafeLabs/fonthammer',
    packages=['fonthammer'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    license='BSD',
    author='Rob Madole'
)

