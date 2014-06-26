# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


# Increase tmdb3's cache time from an hour to a year.
import tmdb3.request
_old__init__ = tmdb3.request.Request.__init__
def _new__init__(self, *args, **kwargs):
    _old__init__(self, *args, **kwargs)
    self.lifetime = 60 * 60 * 24 * 365
tmdb3.request.Request.__init__ = _new__init__
del _new__init__


import tmdb3 as _tmdb3


Movie = _tmdb3.Movie
search_movies = _tmdb3.searchMovie
set_cache = _tmdb3.set_cache
set_key = _tmdb3.set_key

