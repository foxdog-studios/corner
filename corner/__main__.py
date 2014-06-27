from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
import asyncio
import json
import os
import sys

from corner.event_directors import EventDirectors
from corner.events import Events
from corner.films import Films
from corner.languages import Languages
from corner.people import People
from corner.tmdb import TMDBClient, find_tmdb_ids
from corner.utils import default


def main(argv=None):
    api_key = try_load_api_key()
    args = parse_argv(argv=argv, api_key=api_key)
    loop = asyncio.get_event_loop()
    client = TMDBClient.from_path(args.cache_path, args.api_key)

    # Build events
    events = Events.from_csv(args.csv_path, skip_headers=True)

    # Build event directors
    event_directors = EventDirectors.from_events(events)

    # Build films
    film_events = events.filter()
    events_to_films = maps_events_to_films(loop, client, film_events)
    films = Films.from_events(film_events, events_to_films)

    # Build languages
    languages = Languages.from_films(films)

    # Build credits and people
    films_to_credits = maps_films_to_credits(loop, client, films)
    people = People.from_credits(films_to_credits)

    client.save_cache(args.cache_path)
    output(args.output_dir, events, event_directors, films, languages, people)


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


def maps_events_to_films(loop, client, events):
    futures = []
    results = defaultdict(list)

    def append(event, future):
        def callback(future):
            movie = future.result()
            if movie:
                results[event.event_id].append(movie)
        future.add_done_callback(callback)
        futures.append(future)

    for event in events:
        ids = find_tmdb_ids(event)
        if ids:
            for id_ in ids:
                append(event, client.get_movie(id_))
        else:
            append(event, client.search_movie(event.title))

    loop.run_until_complete(asyncio.wait(futures))
    return results


def maps_films_to_credits(loop, client, films):
    results = {}
    def map_film_to_credits(film):
        def callback(credits):
            results[film] = credits.result()
        future = client.get_credits(film.tmdb_film_id)
        future.add_done_callback(callback)
        return future
    loop.run_until_complete(asyncio.wait(map(map_film_to_credits, films)))
    return results


def output(output_dir, events, event_directors, films, languages, people):
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    events.dump_csv(output_dir)
    event_directors.dump_csv(output_dir)
    films.dump_csv(output_dir)
    languages.dump_csv(output_dir)
    people.dump_csv(output_dir)


if __name__ == '__main__':
    sys.exit(main())

