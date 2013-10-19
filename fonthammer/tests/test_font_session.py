import pytest
from null import Null

from fonthammer.api import Font


def test_yields_font():
    """
    A new session will yield the font so we can work with it
    """
    with Font.session() as font:
        assert isinstance(font, Font)


def test_font_reports_closed():
    """
    The font knows that it's closed.
    """
    with Font.session() as font:
        pass

    assert font.closed == True


def test_replace_fontforge_instance():
    """
    After it's closed, you no longer have access the fontforge instance.
    """
    with Font.session() as font:
        pass

    assert font.fontforge_instance.call == Null

    assert font.fontforge_instance == Null
