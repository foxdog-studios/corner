from corner.cast_credit import CastCredit
from corner.crew_credit import CrewCredit
from corner.person import Person
from corner.utils import csv_writer

__all__ = ['People']


class People:
    def __init__(self, people):
        self.people = people

    def dump_csv(self, output_dir):
        with csv_writer(output_dir / 'people.csv') as writer:
            for person in sorted(self.person, key=lambda p: p.tmdb_person_id):
                person.dump_csv(writer)

    @classmethod
    def from_credits(cls, credits):
        people = {}

        for film, credits in credits.items():
            for cast_credit in credits['cast']:
                person_id = cast_credit['id']
                if person_id not in people:
                    people[person_id] = Person(cast_credit)
                person = people[person_id]
                credit = CastCredit(film, cast_credit, person)
                film.cast_credits.add(credit)
                person.cast_credits.add(credit)

            for crew_credit in credits['crew']:
                person_id = crew_credit['id']
                if person_id not in people:
                    people[person_id] = Person(crew_credit)
                person = people[person_id]
                credit = CrewCredit(film, crew_credit, people[person_id])
                film.crew_credits.add(credit)
                person.crew_credits.add(credit)

        return cls(set(people.values()))

