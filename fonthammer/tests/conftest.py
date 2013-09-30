from os import listdir
from os.path import join, dirname

import pytest


class SVGFiles(object):

    """
    SVG files for use while testing.

    """
    def __init__(self, svg_directory):
        self.svg_directory = svg_directory

        self._svg_files = []

        for filename in listdir(svg_directory):
            self._svg_files.append(join(
                svg_directory, filename))

    @property
    def first(self):
        return self._svg_files[0]


class TTFFiles(object):

    """
    TTF files.

    """


@pytest.fixture(scope='module')
def svg_files():
    return SVGFiles(join(dirname(__file__), 'files', 'svg'))
