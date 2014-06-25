from argparse import ArgumentParser
from pathlib import Path
import csv
import sys

from corner.directors_builder import DirectorsBuilder
from corner.events_builder import EventsBuilder
from corner.output import output
from corner.utils import defaults


def main(argv=None):
    args = parse_argv(argv=argv)
    rows = load_csv(args.input_path)
    directors_builder = DirectorsBuilder(rows)
    events_builder = EventsBuilder(directors_builder, rows)
    output(
        events_builder.events,
        directors_builder.directors,
        args.output_dir,
    )


@defaults(argv=lambda: sys.argv)
def parse_argv(argv=None):
    parser = ArgumentParser()
    parser.add_argument('input_path', type=Path)
    parser.add_argument('output_dir', type=Path)
    return parser.parse_args(args=argv[1:])


def load_csv(csv_path):
    with csv_path.open(newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        return [row for row in csv_reader]


if __name__ == '__main__':
    sys.exit(main())

