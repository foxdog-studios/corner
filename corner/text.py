__all__ = ['fix_text']


_CHARACTER_MAPS = [
    {
        ' ≥': '³',
        '¡': 'á',
        '·': 'á',
        '¸': 'ü',
        '¿': 'À',
        'Á': 'ç',
        'Â': 'å',
        'Ê': 'æ',
        'Ë': 'è',
        'Í': 'ê',
        'Ï': 'ì',
        'Ó': 'î',
        'Ô': 'ï',
        'Ö': '…',
        'Ù': 'ô',
        'Û': 'ó',
        'ä': 'Š',
        'é': 'ž',
        'í': '’',
        'ñ': '–',
        'ö': 'š',
        'ÿ': 'Ø',
        '˘': 'ù',
        '˙': 'ú',
        '˚': 'û',
        '˝': 'ý',
        '‘': 'Ō',
        '‚': 'â',
        '‡': 'à',
        '‹': 'Ü',
        '⁄': 'Ú',
        '≈': 'Å',
        'ﬂ': 'ß',
    },
    {
        '°': '¡',
        'È': 'é',
        'Ì': 'í',
        'Ò': 'ñ',
        'ë': '‘',
        '÷': 'ö',
        'ø': '¿',
        'ˆ': 'ö',
        '”': 'Ó',
        '‰': 'ä',
    },
    {
        '¯': 'ø',
        'Î': 'ë',
    },
]


def fix_text(text):
    text = text.strip()
    for map_ in _CHARACTER_MAPS:
        for old, new in map_.items():
            text = text.replace(old, new)
    return text


def validate():
    for i, map_ in enumerate(_CHARACTER_MAPS):
        for new in map_.values():
            for future_map in CHARACTER_MAPS[i:]:
                assert new not in future_map, new

