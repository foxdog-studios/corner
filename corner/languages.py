from corner.language import Language
from corner.utils import csv_writer


__all__ = ['Languages']


class Languages:
    def __init__(self, languages):
        self._languages = languages

    def dump_csv(self, output_dir):
        with csv_writer(output_dir / 'languages.csv') as writer:
            writer.writerow(['iso_639_1', 'Name'])
            for language in sorted(self._languages, key=lambda l: l.iso_639_1):
                language.dump_csv(writer)

    @classmethod
    def from_films(cls, films):
        languages = {}
        for film in films:
            for tmdb_language in film.tmdb_film['spoken_languages']:
                id_ = tmdb_language['iso_639_1']
                if id_ not in languages:
                    languages[id_] = Language(tmdb_language)
                language = languages[id_]
                language.spoken_in.add(film)
                film.spoken_languages.add(language)
        return cls(set(languages.values()))

