from collections import ChainMap, defaultdict
from itertools import chain
from urllib.parse import urlencode, urlunparse
import asyncio
import json
import pickle

import aiohttp

from corner.utils import default

__all__ = ['TMDBClient', 'find_tmdb_ids']


loop = asyncio.get_event_loop()


_EVENTS_MAP = {
     21315: {278122}, # Un garibaldino al convento
    100265: {166085}, # Menú degustación
    104012: {253332}, # Pulp: a Film about Life, Death & Supermarkets
    104909: {   252}, # Willy Wonka & the Chocolate Factory
}


def find_tmdb_ids(event):
    return _EVENTS_MAP.get(event.event_id)


class TMDBClient:
    def __init__(self, cache, api_key, api_version=None, language=None,
                 netloc=None, scheme=None, max_connections=10):
        self._sem = asyncio.Semaphore(max_connections)
        self.cache = cache
        self.api_key = api_key
        self.api_version = str(default(api_version, 3))
        self.language = default(language, 'en')
        self.netloc = default(netloc, 'api.themoviedb.org')
        self.scheme = default(scheme, 'https')

    @asyncio.coroutine
    def _get(self, *path, **query):
        url = self._make_url(*path, **query)
        if url in self.cache['urls']:
            return self.cache['urls'][url]
        with (yield from self._sem):
            response = yield from aiohttp.request('GET', url)
            data = yield from response.read_and_close()
        print(url)
        result = json.loads(data.decode('utf-8'))
        self.cache['urls'][url] = result
        return result

    def _make_url(self, *path, **query):
        path = '/'.join(chain([self.api_version], map(str, path)))
        query = urlencode(sorted(chain(
            [('api_key', self.api_key), ('language', self.language)],
            query.items()
        )))
        return urlunparse((self.scheme, self.netloc, path, '', query, ''))

    def get_credits(self, *args, **kwargs):
        return asyncio.async(self._get_credits(*args, **kwargs))

    @asyncio.coroutine
    def _get_credits(self, movie_id):
        return (yield from self._get('movie', movie_id, 'credits'))

    def get_movie(self, *args, **kwargs):
        return asyncio.async(self._get_movie(*args, **kwargs))

    @asyncio.coroutine
    def _get_movie(self, id_):
        if id_ in self.cache['movies']:
            return self.cache['movies'][id_]
        movie = yield from self._get('movie', id_)
        self.cache['movies'][movie['id']] = movie
        return movie

    def search_movie(self, *args, **kwargs):
        return asyncio.async(self._search_movie(*args, **kwargs))

    @asyncio.coroutine
    def _search_movie(self, query, page=None):
        query = {'query': query}
        def set_if(key, value):
            if value is not None:
                query[key] = value
        set_if('page', page)
        data = yield from self._get('search', 'movie', **query)
        if 'results' in data and data['results']:
            return (yield from self.get_movie(data['results'][0]['id']))


    def save_cache(self, cache_path):
        with cache_path.open('wb') as cache_file:
            pickle.dump(self.cache, cache_file, pickle.HIGHEST_PROTOCOL)

    @classmethod
    def from_path(cls, cache_path, *args, **kwargs):
        if cache_path.exists():
            with cache_path.open('rb') as cache_file:
                cache = pickle.load(cache_file)
        else:
            cache = defaultdict(dict)
        return cls(cache, *args, **kwargs)

