__all__ = [ 'Language']


class Language:
    def __init__(self, tmdb_language):
        self.spoken_in = set()
        self.tmdb_language = tmdb_language
        self.iso_639_1 = tmdb_language['iso_639_1']
        self.name = tmdb_language['name']

    def dump_csv(self, writer):
        writer.writerow([
            self.iso_639_1,
            self.name,
        ])

