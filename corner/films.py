# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import unicodecsv

from corner.film import Film
from corner.tmdb_films import find_tmdb_films


__all__ = ['Films']


class Films(object):
    film_class = Film

    def __init__(self, films):
        self._films = films

    def dump_csv(self, path):
        with open(path, 'w') as file_:
            writer = unicodecsv.writer(file_)
            writer.writerow([
                'tmdb_id',
                'event_id',
                'title',
            ])
            for film in self._films:
                film.dump_csv(writer)

    @classmethod
    def from_events(cls, events):
        films = set()
        for event in events:
            try:
                for tmdb_film in find_tmdb_films(event):
                    film = cls.film_class(event, tmdb_film)
                    films.add(film)
            except ValueError as error:
                print(error, file=sys.stderr)
        return cls(films)

