import csv


def output(events, output_dir):
    if not output_dir.is_dir():
        output_dir.mkdir(parents=True)

    events_path = output_dir / 'events.csv'

    with events_path.open('w', newline='') as events_file:
        events_csv = csv.writer(events_file)


        # Headers
        events_csv.writerow([
            'ID',
            'Title',
            'Alternative title',
            'Year released',
        ])

        for event in sorted(events, key=lambda e: e.id_):
            events_csv.writerow([
                event.id_,
                event.title,
                event.alternative_title,
                event.year_released,
            ])

