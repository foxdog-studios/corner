import sys

from corner.film import Film
from corner.utils import csv_writer


__all__ = ['Films']


class Films(object):
    film_class = Film

    def __init__(self, films):
        self._films = films

    def dump_csv(self, path):
        with csv_writer(path) as writer:
            writer.writerow([
                'event_id',
                'tmdb_id',
                'title',
                'original_title',
                'release_date',
                # 'certificate',
                #'director',
                #'languages',
                'run_time',
                #'country_of_origin',
            ])

            for film in self._films:
                film.dump_csv(writer)

    @classmethod
    def from_events(cls, events, tmdb_movies):
        return cls({cls.film_class(event, tmdb_movies[event.id])
                    for event in events})
