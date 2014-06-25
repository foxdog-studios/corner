from corner.event_builder import EventBuilder


__all__ = ['EventsBuilder']


class EventsBuilder:
    def __init__(self, directors_builder, rows):
        self.events = []
        self.event_builders = []

        ids = set()

        for row in rows:
            event_builder = EventBuilder(directors_builder, row)

            if event_builder.id_ in ids:
                raise ValueError('duplicate id {}'.format(id_))
            ids.add(event_builder.id_)

            self.events.append(event_builder.event)
            self.event_builders.append(event_builder)

