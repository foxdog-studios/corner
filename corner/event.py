# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from corner.text import fix_text

__all__ = ['Rows']


class Event(object):
    def __init__(self, raw_row):
        self._raw_row = raw_row
        self.raw_id = raw_row[0]
        self.raw_title = raw_row[1]

        self.id = self._build_id()
        self.title = self._build_title()

    def __repr__(self):
        return 'Event({!r})'.format(self._raw_row)

    def __str__(self):
        return self.title.encode('ascii', errors='replace')

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def _build_id(self):
        return int(self.raw_id.strip())

    def _build_title(self):
        return fix_text(self.raw_title)

