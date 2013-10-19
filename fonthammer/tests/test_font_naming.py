import sys
import pytest

from mock import patch
import fontforge

from fonthammer.api import Font, Glyph
from fonthammer.exceptions import GlyphCodeError, SaveFailed
from fonthammer.presets.default import DefaultPreset


def test_get_font_name(font_with_glyph):
    """
    Can get the font name.
    """
    assert font_with_glyph.postscript_name == 'FontHammerUntitled-Regular'
    assert font_with_glyph.name == 'FontHammer Untitled Regular'
    assert font_with_glyph.family == 'FontHammer Untitled'
    assert font_with_glyph.style == 'Regular'


def test_set_font_name(font_with_glyph):
    """
    Set the font name.
    """
    font_with_glyph.name = 'A Regular'

    assert font_with_glyph.name == 'A Regular'

    font_with_glyph.family = 'A'

    assert font_with_glyph.family == 'A'

    assert font_with_glyph.style == 'Regular'


def test_set_postscript_name(font_with_glyph):
    """
    Setting the postscript name forces spaces to be removed.
    """
    font_with_glyph.postscript_name = 'A Family Regular'

    assert font_with_glyph.postscript_name == 'AFamilyRegular'
