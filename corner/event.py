from contextlib import suppress

from corner.text import fix_text
from corner.utils import csv_bool


__all__ = ['Event']


_CERTIFICATES = {
    'U',
    'PG',
    '12A',
    '12',
    '15',
    '18',
}


class Event(object):
    def __init__(self, raw_row):
        self.raw_row = raw_row
        self.raw_event_id = raw_row[0]
        self.raw_title = raw_row[1]
        self.raw_alternative_title = raw_row[2]
        self.raw_release_year = raw_row[3]
        self.raw_certificate = raw_row[4]
        self.raw_directors = raw_row[5]
        self.raw_languages = raw_row[6]
        self.raw_duration = raw_row[7]
        self.raw_country_of_origin = raw_row[8]
        self.raw_actors = raw_row[9]

        self.event_id = int(fix_text(self.raw_event_id))
        self.title = fix_text(self.raw_title)
        self.alternative_title = fix_text(self.raw_alternative_title)
        self.release_year = self._parse_release_year()
        self.certificate = fix_text(self.raw_certificate)
        self.directors = fix_text(self.raw_directors)
        self.languages = fix_text(self.raw_languages)
        self.duration = self._parser_duration()
        self.country_of_origin = fix_text(self.raw_country_of_origin)
        self.actors = fix_text(self.raw_actors)
        self.is_live = self._parse_is_live()

    def _parse_release_year(self):
        return self._try_parse_int(self.raw_release_year)

    def _parse_certificate(self):
        certificate = fix_text(self.raw_certificate)
        if certificate in _CERTIFICATES:
            return certificate

    def _parser_duration(self):
        return self._try_parse_int(self.raw_duration)

    def _parse_is_live(self):
        return self.raw_certificate == 'live'

    def _try_parse_int(self, text):
        with suppress(ValueError):
            return int(fix_text(text))

    def __repr__(self):
        return 'Event({!r})'.format(self.raw_row)

    def __str__(self):
        return self.title

    def dump_csv(self, writer):
        writer.writerow([
            self.event_id,
            self.title,
            self.alternative_title,
            self.release_year,
            self.certificate,
            self.directors,
            self.languages,
            self.duration,
            self.country_of_origin,
            self.actors,
            csv_bool(self.is_live),
        ])

