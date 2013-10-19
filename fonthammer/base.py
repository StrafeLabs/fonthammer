from functools import wraps
from contextlib import contextmanager

import py
from py.path import local
from null import Null

from fonthammer.presets.default import DefaultPreset
from fonthammer.exceptions import GlyphCodeError, SaveFailed

try:
    import fontforge
except ImportError:   # pragma: no cover
    raise RuntimeError('Unable to import the FontForge Python extension. '
        'For FontHammer to operate this needs to be installed.')


DEFAULT_FAMILY_NAME = 'FontHammer Untitled'
DEFAULT_STYLE = 'Regular'
DEFAULT_FONT_NAME = '{} {}'.format(DEFAULT_FAMILY_NAME, DEFAULT_STYLE)
DEFAULT_POSTSCRIPT_NAME = '{}-{}'.format(DEFAULT_FAMILY_NAME, DEFAULT_STYLE)


class Font(object):

    """
    Main interface for working with the FontHammer API.

    """
    def __init__(self, existing_font=None, preset=None):
        self._ff_messages = []

        if existing_font:
            with self._captures_messages():
                self._ff = fontforge.open(existing_font)
        else:
            self._ff = fontforge.font()

            self.name = DEFAULT_FONT_NAME
            self.family = DEFAULT_FAMILY_NAME
            self.postscript_name = DEFAULT_POSTSCRIPT_NAME

            self.apply_preset(preset or DefaultPreset)

        self.closed = False

    def __len__(self):
        return len([i for i in self.glyphs])

    @classmethod
    @contextmanager
    def session(cls, *args, **kwargs):
        """
        Context manager that automatically closes the font.

        This convenient function allows you to make the same call that you
        would to ``Font()`` constructor but closes the ``fontforge.font``
        instance once the context manager exits, freeing up memory.
        """
        font = cls(*args, **kwargs)
        yield font
        font.close()
        font._ff = Null

    @contextmanager
    def _captures_messages(self):
        """
        Context manager that captures output to stdout and stderr.
        """
        capture = py.io.StdCaptureFD()

        yield

        out, err = capture.reset()

        if out or err:
            self._ff_messages.append((out, err))

    @property
    def fontforge_instance(self):
        """
        Access the underlying FontForge :class:`fontforge` instance.
        """
        return self._ff

    @property
    def fontforge_messages(self):
        """
        Get any messages generated from interacting with FontForge.
        """
        return self._ff_messages

    def close(self):
        """
        Closes the fontforge.font instance.
        """
        self.closed = True
        self._ff.close()

    def apply_preset(self, preset):
        """
        Set a group of properties on the underlying fontforge.font object.

        :param fonthammer.preset.base.Preset preset:
        """
        for attr, val in preset.items():
            setattr(self._ff, attr, val)

    def add_glyph(self, glyph_code, glyph_file, glyph_name=None):
        """
        Import outlines from a file and create a new glyph on this font.

        :param unicode glyph_code: single unicode character to map the glyph to
        :param glyph_file: location of a file to import outlines from
        :param glyph_name: optional name for the glyph, for example the
            '-' character should have the name 'minus'
        """
        if not isinstance(glyph_code, unicode):
            raise GlyphCodeError('The glyph code must be unicode instance.')

        if not glyph_name:
            glyph_name = hex(ord(glyph_code))[2:].upper()

        glyph = self._ff.createChar(
            ord(glyph_code),
            glyph_name
        )

        glyph.importOutlines(glyph_file)

        glyph.left_side_bearing = 15
        glyph.right_side_bearing = 15

        return Glyph(glyph)

    def save(self, location):
        """
        Save a font file using FontForge to location.
        """
        with self._captures_messages():
            self._ff.generate(location)

        if not local(location).check():
            raise SaveFailed(location)

    @property
    def postscript_name(self):
        return self._ff.fontname

    @postscript_name.setter
    def postscript_name(self, value):
        self._ff.fontname = value.replace(' ', '')

    @property
    def name(self):
        return self._ff.fullname

    @name.setter
    def name(self, value):
        self._ff.fullname = value

    @property
    def family(self):
        return self._ff.familyname

    @family.setter
    def family(self, value):
        self._ff.familyname = value

    @property
    def style(self):
        style = self.name.replace(self.family, '').strip()

        return style or DEFAULT_STYLE

    @property
    def glyphs(self):
        for glyph in self._ff.glyphs():
            yield Glyph(glyph)


class Glyph(object):

    """
    A single glyph.

    """
    def __init__(self, ff_glyph):
        self._ff_glyph = ff_glyph

    @property
    def name(self):
        return self._ff_glyph.glyphname

    @property
    def character(self):
        return unichr(self._ff_glyph.unicode)
