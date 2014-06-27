from corner.credit import Credit


__all__ = ['CrewCredit']


class CrewCredit(Credit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = self.credit['job']

    def dump_csv(self, writer):
        writer.writerow([
            self.tmdb_film_id,
            self.tmdb_person_id,
            self.job,
        ])

