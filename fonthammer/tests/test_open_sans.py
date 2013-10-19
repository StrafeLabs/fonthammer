import sys
import pytest

from mock import patch
import fontforge

from fonthammer.api import Font, Glyph
from fonthammer.exceptions import GlyphCodeError, SaveFailed
from fonthammer.presets.default import DefaultPreset


@pytest.fixture
def regular(open_sans_files):
    return Font(open_sans_files.get('OpenSans-Regular.ttf'))


@pytest.fixture
def bold(open_sans_files):
    return Font(open_sans_files.get('OpenSans-Bold.ttf'))


@pytest.fixture
def italic(open_sans_files):
    return Font(open_sans_files.get('OpenSans-Italic.ttf'))


def test_open_sans_font_names(regular, bold, italic):
    """
    Suite of smoke tests on the Open Sans font.
    """
    assert regular.postscript_name == 'OpenSans'
    assert regular.name == 'Open Sans'
    assert regular.family == 'Open Sans'
    assert regular.style == 'Regular'

    assert bold.postscript_name == 'OpenSans-Bold'
    assert bold.name == 'Open Sans Bold'
    assert bold.family == 'Open Sans'
    assert bold.style == 'Bold'

    assert italic.postscript_name == 'OpenSans-Italic'
    assert italic.name == 'Open Sans Italic'
    assert italic.family == 'Open Sans'
    assert italic.style == 'Italic'


def test_number_of_glyphs(regular, bold, italic):
    """
    Detects the number of glyphs in a font.
    """
    expected_glyphs = 938

    assert len(regular) == expected_glyphs
    assert len(bold) == expected_glyphs
    assert len(italic) == expected_glyphs
