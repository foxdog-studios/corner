from corner.credit import Credit


class CastCredit(Credit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character = self.credit['character']

    def dump_csv(self, writer):
        writer.writerow([
            self.tmdb_film_id,
            self.tmdb_person_id,
            self.character,
        ])

