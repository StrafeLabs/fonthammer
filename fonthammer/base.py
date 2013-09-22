from fonthammer.presets.default import DefaultPreset
from fonthammer.exceptions import GlyphCodeError

try:
    import fontforge
except ImportError:
    raise RuntimeError('Unable to import the FontForge Python extension. '
        'For FontHammer to operate this needs to be installed. See X')


class Font(object):

    """
    Main interface for working with the FontHammer API.

    """
    def __init__(self):
        self._ff = fontforge.font()
        self.apply_preset(DefaultPreset)

    @property
    def fontforge_instance(self):
        """
        Access the underlying FontForge :class:`fontforge` instance.
        """
        return self._ff

    def apply_preset(self, preset):
        for attr, val in preset.items():
            setattr(self._ff, attr, val)

    def add_glyph(self, glyph_code, glyph_file, glyph_name=None):
        if not isinstance(glyph_code, unicode):
            raise GlyphCodeError('The glyph code must be unicode instance.')

        glyph = self._ff.createChar(glyph_code, glyph_name)

        glyph.importOutlines(glyph_file)

        glyph.left_side_bearing = 15
        glyph.right_side_bearing = 15
