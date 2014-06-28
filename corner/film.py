from corner.utils import csv_bool, zero_to_none


__all__ = ['Film']


class Film(object):
    def __init__(self, event, tmdb_film):
        self.cast_credits     = set()
        self.crew_credits     = set()
        self.spoken_languages = set()

        self.event          = event
        self.tmdb_film      = tmdb_film

        self.event_id       = event.event_id
        self.tmdb_film_id   = tmdb_film['id']
        self.title          = tmdb_film['title']

        self.adult          = tmdb_film['adult']
        self.backdrop_path  = tmdb_film['backdrop_path']
        self.budget         = zero_to_none(tmdb_film['budget'])
        self.homepage       = tmdb_film['homepage']
        self.imdb_id        = tmdb_film['imdb_id']
        self.original_title = tmdb_film['original_title']
        self.overview       = tmdb_film['overview']
        self.popularity     = tmdb_film['popularity']
        self.poster_path    = tmdb_film['poster_path']
        self.release_date   = tmdb_film['release_date']
        self.revenue        = zero_to_none(tmdb_film['revenue'])
        self.runtime        = zero_to_none(tmdb_film['runtime'])
        self.status         = tmdb_film['status']
        self.tagline        = tmdb_film['tagline']
        self.vote_average   = tmdb_film['vote_average']
        self.vote_count     = tmdb_film['vote_count']

    def dump_csv_film(self, writer):
        writer.writerow([
            self.event.event_id,
            self.tmdb_film_id,
            self.title,

            csv_bool(self.adult),
            self.backdrop_path,
            self.budget,
            self.homepage,
            self.imdb_id,
            self.original_title,
            self.overview,
            self.popularity,
            self.poster_path,
            self.release_date,
            self.revenue,
            self.runtime,
            self.status,
            self.tagline,
            self.vote_average,
            self.vote_count,
        ])

    def dump_csv_cast_credits(self, writer):
        for cast_credits in sorted(self.cast_credits,
                                   key=lambda cc: cc.tmdb_person_id):
            cast_credits.dump_csv(writer)

    def dump_csv_crew_credits(self, writer):
        for crew_credits in sorted(self.crew_credits,
                                   key=lambda cc: cc.tmdb_person_id):
            crew_credits.dump_csv(writer)

    def dump_csv_spoken_languages(self, writer):
        for language in sorted(self.spoken_languages,
                               key=lambda l: l.iso_639_1):
            writer.writerow([
                self.tmdb_film_id,
                language.iso_639_1,
            ])

