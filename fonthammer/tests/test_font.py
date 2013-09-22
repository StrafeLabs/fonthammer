import pytest

from fonthammer.api import Font
from fonthammer.exceptions import GlyphCodeError
from fonthammer.presets.default import DefaultPreset


def test_apply_preset():
    """
    A new font will have the default presets applied.
    """
    font = Font()

    attributes = DefaultPreset.items()

    for attr, val in attributes:
        assert getattr(font.fontforge_instance, attr) == val


def test_add_glyph_requires_unicode(svg_files):
    """
    The add_glyph method requires unicode.
    """
    font = Font()

    with pytest.raises(GlyphCodeError):
        font.add_glyph("f", svg_files.first)
