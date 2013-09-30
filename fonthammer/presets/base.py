def _only_preset_attributes(preset, ignore=[]):
    """
    Used to filter out attributes that are not part of the preset.
    """
    for attr in dir(preset):
        # It's in our ignore list
        if attr in ignore:
            continue
        val = getattr(preset, attr)
        if callable(val):
            continue
        # Double underscore attribute, skip these
        if attr.startswith('__'):
            continue
        yield attr


class Preset(object):

    """
    Common methods for all font presets.

    """
    @classmethod
    def items(cls):
        """
        Tuple of tuples suitable for setting on a fontforge.font object.
        """
        attrs = []
        for attr in _only_preset_attributes(cls, ignore=['os2']):
            attrs.append(
                (attr, getattr(cls, attr))
            )

        # Grab the OS2 attributes and expand those into "os2_" attributes
        for os2attr in _only_preset_attributes(cls.os2):
            attrs.append(
                ('os2_{0}'.format(os2attr), getattr(cls.os2, os2attr))
            )

        return attrs
