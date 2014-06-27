__all__ = ['Film']


class Film(object):
    def __init__(self, event, tmdb_film):
        self.event = event
        self.tmdb_film = tmdb_film

    def dump_csv(self, writer):
        writer.writerow([
            self.tmdb_film['id'],
            self.event.id,
            self.tmdb_film['title'],
            self.tmdb_film['original_title'],
            self.tmdb_film['release_date'],
            # self.tmdb_film.releases['uk'].certificate,
            # self.tmdb_film.crew.director,
            # self.tmdb_film.languages....,
            self.tmdb_film['runtime'],
            # country_of_origin,
        ])

