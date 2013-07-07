from unittest import TestCase

from fonthammer.api import Font
from fonthammer.presets.default import DefaultPreset


class FontTest(TestCase):

    """
    FontHammer main font object tests.

    """
    def test_apply_preset(self):
        """
        A new font will have the default presets applied.
        """
        font = Font()

        attributes = DefaultPreset.items()

        for attr, val in attributes:
            self.assertEqual(
                getattr(font.fontforge_instance, attr),
                val)
