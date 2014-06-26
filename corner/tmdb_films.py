# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from corner import tmdb3


__all__ = ['find_tmdb_films']


_EVENTS_MAP = {
    100265: {166085}, # Menú degustación
    104012: {253332}, # Pulp: a Film about Life, Death & Supermarkets
    104909: {   252}, # Willy Wonka & the Chocolate Factory
}


def find_tmdb_films(event):
    if event.id in _EVENTS_MAP:
        return {tmdb3.Movie(tmdb_id) for tmdb_id in _EVENTS_MAP[event.id]}
    try:
        return {tmdb3.search_movies(event.title)[0]}
    except IndexError:
        raise ValueError('No TMdb film for {!r}'.format(event))

