from collections import defaultdict
from contextlib import contextmanager

from corner.event_director import EventDirector
from corner.text import fix_text
from corner.utils import csv_writer


__all__ = ['EventDirectors']


_DIRECTOR_MAP = {
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


class EventDirectors:
    def __init__(self, event_directors):
        self._event_directors = event_directors

    def dump_csv(self, output_dir):
        @contextmanager
        def event_directors_writer():
            with csv_writer(output_dir / 'event_directors.csv') as writer:
                yield writer

        @contextmanager
        def event_directed_by_writer():
            with csv_writer(output_dir / 'event_directed_by.csv') as writer:
                yield writer

        with event_directors_writer() as writer:
            writer.writerow(['event_director_id', 'name'])
            for event_director in sorted(self._event_directors,
                                         key=lambda e: e.event_director_id):
                event_director.dump_csv(writer)

        rows =[]
        for event_director in self._event_directors:
            for event in event_director.events:
                rows.append((event.event_id, event_director.event_director_id))
        rows.sort()

        with event_directed_by_writer() as writer:
            writer.writerow(['event_id', 'event_director_id'])
            writer.writerows(rows)


    @classmethod
    def from_events(cls, events):
        directors = defaultdict(set)
        for event in events:
            names = cls.parse_names(event.raw_directors)
            for name in names:
                directors[name].add(event)
        return cls({EventDirector(i, name, events)
                    for i, (name, events) in
                    enumerate(sorted(directors.items()), start=1)})

    @staticmethod
    def parse_names(text):
        names = set()
        for token in text.split(', '):
            token = token.strip()
            if token:
                if token in _DIRECTOR_MAP:
                    token_names = _DIRECTOR_MAP[token]
                else:
                    token_names = {fix_text(token)}
                names |= token_names
        return names

