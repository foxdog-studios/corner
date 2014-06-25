# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import csv
import json
import os
import sys

from corner.tmdb3_wrapper import tmdb3


def main(argv=None):
    key = try_load_key()
    args = parse_argv(argv=argv, key=key)
    configure_tmdb3(args)
    rows = load_csv(args.input_path, skip_headers=True)

    for title in (row[1] for row in rows):
        try:
            movie = tmdb3.searchMovie(title)[0]
        except IndexError:
            continue
        print(movie.id)


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
    parser.add_argument('input_path')
    parser.add_argument('output_dir')

    return parser.parse_args(args=argv[1:])


def configure_tmdb3(args):
    tmdb3.set_key(args.key)
    if args.engine == 'file':
        tmdb3.set_cache(filename=args.filename)
    else:
        tmdb3.set_cache('null')


def load_csv(csv_path, skip_headers=False):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        if skip_headers:
            next(csv_reader)
        return list(csv_reader)


if __name__ == '__main__':
    sys.exit(main())

