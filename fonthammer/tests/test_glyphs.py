import pytest

from fonthammer.api import Font, Glyph


def test_access_glyphs(font_with_glyph):
    """
    Can access the glyphs from the font.
    """
    glyphs = font_with_glyph.glyphs


def test_default_glyph_name(svg_files):
    """
    Default glyph names.
    """
    font = Font()

    font.add_glyph(u'\uf000', svg_files.first)

    glyph = font.glyphs.next()

    assert glyph.name == 'F000'


def test_default_glyph_name(svg_files):
    """
    Explicit glyph names.
    """
    font = Font()

    font.add_glyph(u'\uf000', svg_files.first, glyph_name='glyph')

    glyph = font.glyphs.next()

    assert glyph.name == 'glyph'


def test_glyph_character(svg_files):
    """
    Access to the glyph unicode character.
    """
    font = Font()

    font.add_glyph(u'\uf000', svg_files.first, glyph_name='glyph')

    glyph = font.glyphs.next()

    assert glyph.character == u'\uf000'
