# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


__all__ = ['fix_text']


_CHARACTER_MAPS = [
    {
        u' ≥': u'³',
        u'¡': u'á',
        u'·': u'á',
        u'¸': u'ü',
        u'¿': u'À',
        u'Á': u'ç',
        u'Â': u'å',
        u'Ê': u'æ',
        u'Ë': u'è',
        u'Í': u'ê',
        u'Ï': u'ì',
        u'Ó': u'î',
        u'Ô': u'ï',
        u'Ö': u'…',
        u'Ù': u'ô',
        u'Û': u'ó',
        u'ä': u'Š',
        u'é': u'ž',
        u'í': u'’',
        u'ñ': u'–',
        u'ö': u'š',
        u'ÿ': u'Ø',
        u'˘': u'ù',
        u'˙': u'ú',
        u'˚': u'û',
        u'˝': u'ý',
        u'‘': u'Ō',
        u'‚': u'â',
        u'‡': u'à',
        u'‹': u'Ü',
        u'⁄': u'Ú',
        u'≈': u'Å',
        u'ﬂ': u'ß',
    },
    {
        u'°': u'¡',
        u'È': u'é',
        u'Ì': u'í',
        u'Ò': u'ñ',
        u'ë': u'‘',
        u'÷': u'ö',
        u'ø': u'¿',
        u'ˆ': u'ö',
        u'”': u'Ó',
        u'‰': u'ä',
    },
    {
        u'¯': u'ø',
        u'Î': u'ë',
    },
]


def fix_text(text):
    text = text.strip()
    for map_ in _CHARACTER_MAPS:
        for old, new in map_.iteritems():
            text = text.replace(old, new)
    return text


def validate():
    for i, map_ in enumerate(_CHARACTER_MAPS):
        for new in map_.values():
            for future_map in CHARACTER_MAPS[i:]:
                assert new not in future_map, new

