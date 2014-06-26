# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import json
import os
import sys

from corner import tmdb3
from corner.events import Events
from corner.films import Films


def main(argv=None):
    key = try_load_key()
    args = parse_argv(argv=argv, key=key)
    configure_tmdb3(args)
    events = Events.from_csv(args.csv_path, encoding='utf-8',
                             skip_headers=True)

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    films = Films.from_events(events.filter())
    films.dump_csv(args.output_dir + '/films.csv')


def try_load_key():
    config_path = os.environ.get('CORNER_CONFIG')
    if config_path:
        with open(config_path) as config_file:
            return json.load(config_file).get('key')


def parse_argv(argv=None, key=None):
    if argv is None:
        argv = sys.argv
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--cache', dest='filename',
                       default='~/.tmdb3cache')
    group.add_argument('-C', dest='engine', default='file',
                       action='store_const', const='null')
    parser.add_argument('-k', '--key', default=key, required=key is None)
    parser.add_argument('csv_path')
    parser.add_argument('output_dir')
    return parser.parse_args(args=argv[1:])


def configure_tmdb3(args):
    tmdb3.set_key(args.key)
    if args.engine == 'file':
        tmdb3.set_cache(filename=args.filename)
    else:
        tmdb3.set_cache('null')


if __name__ == '__main__':
    sys.exit(main())

