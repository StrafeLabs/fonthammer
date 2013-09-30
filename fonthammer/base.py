import py
from py.path import local

from fonthammer.presets.default import DefaultPreset
from fonthammer.exceptions import GlyphCodeError, SaveFailed

try:
    import fontforge
except ImportError:   # pragma: no cover
    raise RuntimeError('Unable to import the FontForge Python extension. '
        'For FontHammer to operate this needs to be installed. See X')


class Font(object):

    """
    Main interface for working with the FontHammer API.

    """
    def __init__(self):
        self._ff = fontforge.font()
        self._ff_messages = []
        self.apply_preset(DefaultPreset)

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

    def apply_preset(self, preset):
        for attr, val in preset.items():
            setattr(self._ff, attr, val)

    def add_glyph(self, glyph_code, glyph_file, glyph_name=None):
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
        capture = py.io.StdCaptureFD()
        self._ff.generate(location)
        out, err = capture.reset()

        if not local(location).check():
            raise SaveFailed(location)

        self._ff_messages.append((out, err))


class Glyph(object):

    """
    A single glyph.

    """
    def __init__(self, ff_glyph):
        self._ff_glyph = ff_glyph

    @property
    def name(self):
        return self._ff_glyph.glyphname
