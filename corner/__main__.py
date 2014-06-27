from argparse import ArgumentParser
from pathlib import Path
import asyncio
import json
import os
import sys

from corner.event_directors import EventDirectors
from corner.events import Events
from corner.films import Films
from corner.tmdb import TMDBClient, find_tmdb_ids
from corner.utils import default


def main(argv=None):
    api_key = try_load_api_key()
    args = parse_argv(argv=argv, api_key=api_key)

    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    events = Events.from_csv(args.csv_path, skip_headers=True)
    client = TMDBClient.from_path(args.cache_path, args.api_key)

    results = {}
    futures = []

    def append(event_id, future):
        def callback(future):
            movie = future.result()
            if movie:
                results[event_id] = movie
        future.add_done_callback(callback)
        futures.append(future)


    film_events = events.filter()

    for i, event in enumerate(film_events):
        ids = find_tmdb_ids(event)
        if ids:
            for id_ in ids:
                append(event.event_id, client.get_movie(id_))
        else:
            append(event.event_id, client.search_movie(event.title))

    loop.run_until_complete(asyncio.wait(futures))
    client.save_cache(args.cache_path)

    event_directors = EventDirectors.from_events(events)
    films = Films.from_events(film_events, results)

    output_dir = args.output_dir
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    events.dump_csv(output_dir)
    event_directors.dump_csv(output_dir)
    films.dump_csv(output_dir)


def try_load_api_key():
    config_path = os.environ.get('CORNER_CONFIG')
    if config_path:
        with open(config_path) as config_file:
            return json.load(config_file).get('api_key')


def parse_argv(argv=None, api_key=None):
    argv = default(argv, sys.argv)

    def to_path(path):
        return Path(os.path.expanduser(path))

    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--cache', dest='cache_path',
                       default='~/.corner.pickle', type=to_path)
    parser.add_argument('-k', '--key', dest='api_key', default=api_key,
                        required=api_key is None)
    parser.add_argument('csv_path', type=to_path)
    parser.add_argument('output_dir', type=to_path)
    return parser.parse_args(args=argv[1:])


if __name__ == '__main__':
    sys.exit(main())

