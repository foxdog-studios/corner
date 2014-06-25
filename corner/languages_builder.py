from corner.language import Language


__all__ = ['LanguagesBuilder']


LANGAUGE_CORRECTIONS = {
    ''                               : None        ,
    "Ch'timi"                        : 'Picard'    ,
    'English (Dubbed)'               : 'English'   ,
    'English (Spanish subtitles)'    : 'English'   ,
    'German [Hessian Dialect]'       : 'German'    ,
    'MorÈ'                           : 'Mossi'     ,
    'Portugese'                      : 'Portuguese',
    'Portugese (Brazilian)'          : 'Portuguese',
    'Silent'                         : None        ,
    'Silent w/ musical accompaniment': None        ,
    'Spain'                          : 'Spanish'   ,
    'Spainsh'                        : 'Spanish'   ,
    'Various languages'              : None        ,
}


class LanguagesBuilder:
    def __init__(self, rows):
        names = set()
        for row in rows:
            for name in row[6].split(','):
                name = name.strip()
                if name:
                    name = LANGAUGE_CORRECTIONS.get(name, name)
                    if name:
                        names.add(name)

        self.languages = [Language(id_, name) for id_, name in
                          enumerate(sorted(names), start=1)]

