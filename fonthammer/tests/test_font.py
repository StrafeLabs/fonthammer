import sys
import pytest

from mock import patch

from fonthammer.api import Font, Glyph
from fonthammer.exceptions import GlyphCodeError, SaveFailed
from fonthammer.presets.default import DefaultPreset


@pytest.fixture
def font_with_glyph(svg_files):
    font = Font()

    font.add_glyph(u'\uf000', svg_files.first)

    return font


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
        font.add_glyph('f', svg_files.first)


def test_add_glyph(svg_files):
    """
    A glyph can be added with valid unicode and SVG file.
    """
    font = Font()

    glyph = font.add_glyph(u'\uf000', svg_files.first)

    assert isinstance(glyph, Glyph)


def test_add_glyph_with_name(svg_files):
    """
    A glyph can be added with a specific name.
    """
    font = Font()

    glyph = font.add_glyph(u'\uf000', svg_files.first, 'a')

    assert glyph.name == 'a'


def test_add_lots_of_glyphs(tmpdir, svg_files):
    """
    A lot of glyphs can be added.
    """
    font = Font()

    for i in range(100):
        glyph_code = unichr(ord(u'\uf000') + i)
        glyph = font.add_glyph(glyph_code, svg_files.first)

    font.save(str(tmpdir.join('file.ttf')))


def test_supports_multiple_versions(tmpdir, font_with_glyph):
    """
    Will support all of the standard formats.
    """
    formats = ['ttf', 'ufo', 'otf', 'svg', 'woff', 'eot']

    for extension in formats:
        filename = tmpdir.join('file.{}'.format(extension))
        font_with_glyph.save(str(filename))

        assert filename.check()


def test_save_ttf(tmpdir, font_with_glyph):
    """
    Can save a TTF.
    """
    ttf_file = tmpdir.join('file.ttf')

    font_with_glyph.save(str(ttf_file))

    assert True == ttf_file.check()


def test_save_captures_output(tmpdir, font_with_glyph):
    """
    If save generates output it gets captured.
    """
    ttf_file = tmpdir.join('file.ttf')
    ttf_file.write('')

    def message(*args, **kwargs):
        sys.stdout.write('out')
        sys.stderr.write('err')

    with patch.object(font_with_glyph, '_ff') as ff:
        ff.generate.side_effect = message

        font_with_glyph.save(str(ttf_file))

    assert font_with_glyph.fontforge_messages[0] == ('out', 'err')


def test_save_fails_to_create_file(tmpdir, font_with_glyph):
    """
    If saving failes to generate the file, an exception is raised.
    """
    with patch.object(font_with_glyph, '_ff'):
        with pytest.raises(SaveFailed) as exc:
            font_with_glyph.save(str(tmpdir.join('file.ttf')))

        assert 'Failed to save font file' in str(exc.value)
