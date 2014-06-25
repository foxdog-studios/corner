__all__ = ['correct']


CHARACTER_CORRECTIONS = [
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
        'í': "'",
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


def _validate():
    for i, round_ in enumerate(CHARACTER_CORRECTIONS):
        for new in round_.values():
            for next_round in CHARACTER_CORRECTIONS[i:]:
                assert new not in next_round, new
_validate()


def correct(text):
    corrections = False
    for round_ in CHARACTER_CORRECTIONS:
        for old, new in round_.items():
            if old in text:
                text = text.replace(old, new)
                corrections = True
    return corrections, text

