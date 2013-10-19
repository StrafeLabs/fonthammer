from os import listdir
from os.path import join, dirname

import pytest


class Files(object):

    """
    Fixture to access files from a given directory.

    """
    def __init__(self, directory):
        self.directory = directory

        self._files = []

        for filename in listdir(directory):
            self._files.append(join(
                directory, filename))

    @property
    def first(self):
        return self._files[0]

    def get(self, name):
        for filename in self._files:
            if name in filename:
                return filename


@pytest.fixture(scope='module')
def svg_files():
    return Files(join(dirname(__file__), 'files', 'svg'))


@pytest.fixture(scope='module')
def open_sans_files():
    return Files(join(dirname(__file__), 'files', 'ttf', 'opensans'))


@pytest.fixture
def font_with_glyph(svg_files):
    from fonthammer.api import Font

    font = Font()

    font.add_glyph(u'\uf000', svg_files.first)

    return font
