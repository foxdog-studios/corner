__all__ = ['EventDirector']


class EventDirector:
    def __init__(self, event_director_id, name, events):
        self.event_director_id = event_director_id
        self.name = name
        self.events = events

    def dump_csv(self, event_directors_writer):
        event_directors_writer.writerow([
            self.event_director_id,
            self.name
        ])

