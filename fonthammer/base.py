from fonthammer.presets.default import DefaultPreset

try:
    import fontforge
except ImportError:
    raise RuntimeError('Unable to import the FontForge Python extension. '
        'For FontHammer to operate this needs to be installed. See X')


class Font(object):

    """
    Main interface an object to working with the FontHammer API.

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
