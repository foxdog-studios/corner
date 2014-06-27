__all__ = ['Film']


class Film(object):
    def __init__(self, event, tmdb_film):
        self.event = event
        self.tmdb_film = tmdb_film

        self.tmdb_id = tmdb_film['id']
        self.title = tmdb_film['title']
        self.original_title = tmdb_film['original_title']
        self.release_date = tmdb_film['release_date']
        self.runtime = tmdb_film['runtime']

    def dump_csv(self, writer):
        writer.writerow([
            self.event.event_id,
            self.tmdb_id,

            self.title,
            self.original_title,
            self.release_date,
            # self.tmdb_film.releases['uk'].certificate,
            # self.tmdb_film.crew.director,
            # self.tmdb_film.languages....,
            self.runtime,
            # country_of_origin,
        ])

