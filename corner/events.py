from corner.event import Event
from corner.events_filter import filter_events
from corner.utils import csv_reader, csv_writer


__all__ = ['Events']


class Events(object):
    def __init__(self, events):
        self._events = events

    def __iter__(self):
        return iter(self._events)

    def filter(self):
        return type(self)(list(filter_events(self._events)))

    def dump_csv(self, path):
        with csv_writer(path) as writer:
            writer.writerow([
                'event_id',
                'title',
                'alternative_title',
                'release_year',
                'certificate',
                'director',
                'language',
                'duration',
                'country_of_origin',
                'actors',
            ])

            def key(event):
                return event.event_id

            for event in sorted(self._events, key=key):
                event.dump_csv(writer)

    @classmethod
    def from_csv(cls, path, skip_headers=False):
        with csv_reader(path) as reader:
            if skip_headers:
                next(reader)
            return cls([Event(row) for row in reader])

