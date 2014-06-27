from corner.text import fix_text


__all__ = ['Event']


class Event(object):
    def __init__(self, raw_row):
        self._raw_row = raw_row
        self.raw_id = raw_row[0]
        self.raw_title = raw_row[1]

        self.id = int(self.raw_id)
        self.title = fix_text(self.raw_title)

    def __repr__(self):
        return 'Event({!r})'.format(self._raw_row)

    def __str__(self):
        return self.title

