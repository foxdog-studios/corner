from argparse import ArgumentParser
from pprint import pprint
import csv
import sys

from corner.directors_builder import DirectorsBuilder
from corner.events_builder import EventsBuilder
from corner.utils import defaults


def main(argv=None):
    args = parse_argv(argv=argv)
    rows = load_csv(args.csv_path)
    dsb = DirectorsBuilder(rows)
    esb = EventsBuilder(dsb, rows)

    for eb in esb.event_builders:
        print(eb.event.directors)


@defaults(argv=lambda: sys.argv)
def parse_argv(argv=None):
    parser = ArgumentParser()
    parser.add_argument('csv_path')
    return parser.parse_args(args=argv[1:])


def load_csv(csv_path):
    with open(csv_path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        return [row for row in csv_reader]


if __name__ == '__main__':
    sys.exit(main())

