from contextlib import contextmanager
import csv


def output(events, directors, output_dir):
    if not output_dir.is_dir():
        output_dir.mkdir(parents=True)

    directors_path = output_dir / 'directors.csv'
    event_directors_path = output_dir / 'event_directors.csv'
    events_path = output_dir / 'events.csv'

    # Events
    with csv_writer(events_path) as events_csv:
        events_csv.writerow([
            'ID',
            'Title',
            'Alternative title',
            'Year released',
            'Certificate',
            'Preview?',
            'Live?',
        ])

        for event in sorted(events, key=lambda e: e.id_):
            events_csv.writerow([
                event.id_,
                event.title,
                event.alternative_title,
                event.year_released,
                event.certificate,
                csv_bool(event.is_preview),
                csv_bool(event.is_live),
            ])

    # Directors
    with csv_writer(directors_path) as directors_csv:
        directors_csv.writerow([
            'ID',
            'Name',
        ])

        for director in sorted(directors, key=lambda d: d.id_):
            directors_csv.writerow([
                director.id_,
                director.name,
            ])

    # Event directors
    with csv_writer(event_directors_path) as event_directors_csv:
        event_directors_csv.writerow([
            'Event ID',
            'Director ID',
        ])

        for event in sorted(events, key=lambda e: e.id_):
            for director in sorted(event.directors, key=lambda d: d.id_):
                event_directors_csv.writerow([
                    event.id_,
                    director.id_,
                ])


def csv_bool(obj):
    if bool(obj):
        return 1
    else:
        return 0


@contextmanager
def csv_writer(path):
    with path.open('w', newline='') as file_:
        yield csv.writer(file_)

