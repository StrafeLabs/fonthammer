from fonthammer.presets.default import DefaultPreset


def test_can_get_items():
    """
    Font preset tests.
    """
    expected = (
        'encoding',
        'ascent',
        'descent',
        'weight',
        'gasp',
        'gasp_version',
        'hhea_descent',
        'hhea_linegap',
        'os2_codepages',
        'os2_fstype',
        'os2_panose',
        'os2_strikeypos',
        'os2_strikeysize',
        'os2_subyoff',
        'os2_subysize',
        'os2_supyoff',
        'os2_supysize',
        'os2_typolinegap')

    items = DefaultPreset.items()

    assert set(zip(*items)[0]) == set(expected)
