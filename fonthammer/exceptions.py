class FontHammerException(Exception):

    """
    Base exception.

    """
    pass


class GlyphCodeError(FontHammerException):

    """
    Raised when an interaction or representation of a glyph is in error.

    """
    pass


class SaveFailed(FontHammerException):

    """
    Raised when saving a font file to disk fails.

    """
    def __init__(self, location):
        self.message = "Failed to save font file to {}".format(location)

    def __str__(self):
        return self.message
