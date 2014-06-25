from corner.character_corrections import correct
from corner.director_builder import DirectorBuilder


__all__ = ['DirectorsBuilder']


DIRECTOR_CORRECTIONS = {
    #
    # Incorrect spelling or formatting.
    #

    'Al &amp; Al': {
        'AL and AL',
    },
    'Alberto Vendemmiati &amp; Fabrizio Lazzaretti': {
        'Alberto Vendemmiati',
        'Fabrizio Lazzaretti',
    },
    'Aleksandr Mani&#269;': {
        'Aleksandr Manic',
    },
    'Alfonso Albacete &amp; David Menkes': {
        'Alfonso Albacete',
        'David Menkes',
    },
    'Andrew Lau &amp; Alan Mak': {
        'Alan Mak',
        'Wai-keung Lau',
    },
    'Andy and Larry Wachowski': {
        'Andy Wachowski',
        'Larry Wachowski',
    },
    'Bestar Cram &amp; Mike Majoros': {
        'Bestar Cram',
        'Mike Majoros',
    },
    'BenoÓt Delepine': {
        'Benoît Delépine',
    },
    'Carl Boese &amp; Paul Wegener': {
        'Carl Boese',
        'Paul Wegener',
    },
    'Chris Hegedus &amp; DA Pennebaker': {
        'Chris Hegedus',
        'D.A. Pennebaker',
    },
    'Dan Ollman &amp; Sarah Price': {
        'Dan Ollman',
        'Sarah Price',
    },
    'Danny &amp; Oxide Pang': {
        'Danny',
        'Oxide Pang',
    },
    'Deborah Goodman (Deborah Dickson)': {
        'Deborah Dickson',
    },
    'Detlef Sierck (Douglas Sirk)': {
        'Douglas Sirk',
    },
    'Emma Bernard (Opera)': {
        'Emma Bernard',
    },
    'Fernando Meirelles &amp; Nando Olival': {
        'Fernando Meirelles',
        'Nando Olival',
    },
    'Isidro Ortiz &amp; ¿lex OllÈ': {
        'Isidro Ortiz',
        'Àlex Ollé',
    },
    'Paul Wagner &amp; Thupten Tseing': {
    },
    'J¯rgen Leth &amp; Lars von Trier': {
        'Jørgen Leth',
        'Lars von Trier',
    },
    'Ji&#345;Ì B·rta': {
        'Jiří Barta',
    },
    'Ji&#345;Ì Trnka': {
        'Jiří Trnka'
    },
    'Joao Moreira Salles &amp; Katia Lund': {
        'Joao Moreira Salles',
        'Katia Lund',
    },
    'Joe King and Rosie Pedlow': {
        'Joe King',
        'Rosie Pedlow',

    },
    'Ken Fero and Tariq Mehmood': {
        'Ken Fero',
        'Tariq Mehmood',
    },
    'Maurizio Nichetti &amp; Guido Manuli': {
        'Guido Manuli',
        'Maurizio Nichetti',
    },
    'Katsuhiro ‘tono': {
        'Katsuhiro Otono',
    },
    'Mitchell &amp; Kenyon': {
        'James Kenyon',
        'Sagar Mitchell',
    },
    'Nina Pope and Karen Guthrie': {
        'Karent Guthrie',
        'Nina Pope',
    },
    'Olivier Ducastel &amp; Jacques Martineau': {
        'Olivier Ducastel',
        'Jacques Martineau',
    },
    'Olivier Ducastel and Jacques Martineau': {
        'Olivier Ducastel',
        'Jacques Martineau',
    },
    'Paul Wagner &amp; Thupten Tseing': {
        'Paul Wagner',
        'Thupten Tseing',
    },
    'Roger Gual &amp; Julio Wallovits': {
        'Julio Wallovits',
        'Roger Gual',
    },
    'Rupert Jones (Film)': {
        'Rupert Jones',
    },
    'Tareque &amp; Catherine Masud': {
        'Tareque',
        'Catherine Masud',
    },
    'Tom·s GutiÈrrez Alea and Juan Carlos Tabio': {
        'Tomás Gutiérrez Alea',
        'Juan Carlos Tabío',
    },
    'Vicky Funari &amp; Julia Query': {
        'Vicky Funari',
        'Julia Query',
    },
    'Vit Klus·k &amp; Filip Remunda': {
        'Filip Remunda',
        'Vit Klusák',
    },


    #
    # Incorrect directors
    #

    # Cay Wesnigk as the production manager, according to IMDb.
    'Cay Wesnigk and Wolfgang Kissel': {
        'Wolfgang Kissel',
    },


    #
    # Not directors
    #

    '11 of the worldís most au courant directors': set(),
    'Screening as part of the ITV50 season.': set(),
    'Various': set(),
    'Various Directors': set(),
}


class DirectorsBuilder:
    def __init__(self, rows):
        self._by_name = {}
        self.directors = []
        self.director_builders = []

        names = set()
        for row in rows:
            names.update(self.split(row[5]))

        for name in names:
            director_builder = DirectorBuilder(name)
            self._by_name[name] = director_builder
            self.directors.append(director_builder.director)
            self.director_builders.append(director_builder)

    def get_director_builders(self, text):
       return [self._by_name[name] for name in self.split(text)]

    @staticmethod
    def split(text):
        all_directors = set()
        for directors in text.split(', '):
            directors = directors.strip()
            if directors:
                if directors in DIRECTOR_CORRECTIONS:
                    directors = DIRECTOR_CORRECTIONS[directors]
                else:
                    directors = {correct(directors)[1]}
                all_directors |= directors
        return all_directors

