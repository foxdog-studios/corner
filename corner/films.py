import sys

from corner.film import Film
from corner.utils import csv_writer


__all__ = ['Films']


class Films(object):
    film_class = Film

    def __init__(self, films):
        self._films = films

    def dump_csv(self, output_dir):
        with csv_writer(output_dir / 'films.csv') as writer:
            writer.writerow([
                'event_id',
                'tmdb_id',
                'title',

                'adult',
                'backdrop_path',
                'budget',
                'homepage',
                'imdb_id',
                'original_title',
                'overview',
                'popularity',
                'poster_path',
                'release_date',
                'revenue',
                'runtime',
                'status',
                'tagline',
                'vote_average',
                'vote_count',
            ])

            def key(film):
                return film.event_id, film.tmdb_id

            for film in sorted(self._films, key=key):
                film.dump_csv(writer)

    @classmethod
    def from_events(cls, events, tmdb_movies):
        return cls({cls.film_class(event, tmdb_movies[event.event_id])
                    for event in events})

