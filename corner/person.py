__all__ = ['Person']


class Person:
    def __init__(self, tmdb_credit):
        self.cast_credits = set()
        self.crew_credits = set()

        self.tmdb_credit = tmdb_credit

        self.tmdb_person_id = tmdb_credit['id']
        self.name           = tmdb_credit['name']
        self.profile_path   = tmdb_credit['profile_path']

    def dump_csv(self, write):
        write.writerow([
            self.tmdb_person_id,
            self.name,
            self.profile_path,
        ])

