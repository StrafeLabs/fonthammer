from .base import Preset


class DefaultPreset(Preset):
    encoding = 'UnicodeFull'
    ascent = 1536
    descent = 256
    weight = 'Book'
    gasp = ((65535, ('gridfit', 'antialias', 'symmetric-smoothing', 'gridfit+smoothing')),)
    gasp_version = 1
    hhea_descent = -34
    hhea_linegap = 0

    class os2:
        codepages = (1, 0)
        fstype = 4
        panose = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        strikeypos = 1075
        strikeysize = 90
        subyoff = 134
        subysize = 1075
        supyoff = 627
        supysize = 1075
        typolinegap = 0
