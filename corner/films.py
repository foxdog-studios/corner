import sys

from corner.film import Film
from corner.utils import csv_writer


__all__ = ['Films']


class Films(object):
    film_class = Film

    def __init__(self, films):
        self._films = films

    def __iter__(self):
        return iter(self._films)

    def dump_csv(self, output_dir):
        self.dump_csv_films(output_dir)
        self.dump_csv_cast_credits(output_dir)
        self.dump_csv_crew_credits(output_dir)
        self.dump_csv_spoken_languages(output_dir)

    def dump_csv_films(self, output_dir):
        with csv_writer(output_dir / 'films.csv') as writer:
            writer.writerow([
                'event_id',
                'tmdb_film_id',
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
                return film.event_id, film.tmdb_film_id

            for film in sorted(self._films, key=key):
                film.dump_csv_film(writer)

    def dump_csv_cast_credits(self, output_dir):
        with csv_writer(output_dir / 'cast_credits.csv') as writer:
            writer.writerow([
                'tmdb_film_id',
                'tmdb_person_id',
                'character',
            ])

            def key(film):
                return film.tmdb_film_id

            for film in sorted(self._films, key=key):
                film.dump_csv_cast_credits(writer)

    def dump_csv_crew_credits(self, output_dir):
        with csv_writer(output_dir / 'crew_credits.csv') as writer:
            writer.writerow([
                'tmdb_film_id',
                'tmdb_person_id',
                'job',
            ])

            def key(film):
                return film.tmdb_film_id

            for film in sorted(self._films, key=key):
                film.dump_csv_crew_credits(writer)

    def dump_csv_spoken_languages(self, output_dir):
        with csv_writer(output_dir / 'spoken_languages.csv') as writer:
            writer.writerow([
                'tmdb_film_id',
                'iso_639_1',
            ])

            def key(film):
                return film.tmdb_film_id

            for film in sorted(self._films, key=key):
                film.dump_csv_spoken_languages(writer)

    @classmethod
    def from_events(cls, events, tmdb_movies):
        films = set()
        for event in events:
            for tmdb_movie in tmdb_movies[event.event_id]:
                film = cls.film_class(event, tmdb_movie)
                films.add(film)
        return cls(films)

