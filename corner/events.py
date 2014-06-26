# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unicodecsv

from corner.event import Event
from corner.events_filter import filter_events


__all__ = ['Events']


class Events(object):
    def __init__(self, events):
        self._events = events

    def __iter__(self):
        return iter(self._events)

    def filter(self):
        return type(self)(list(filter_events(self._events)))

    @classmethod
    def from_csv(cls, path, encoding=None, skip_headers=False):
        with open(path) as file_:
            reader = unicodecsv.reader(file_, encoding=encoding)
            if skip_headers:
                next(reader)
            return cls(map(Event, reader))

