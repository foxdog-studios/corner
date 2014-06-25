from contextlib import suppress

from corner.certificates import CERTIFICATES
from corner.character_corrections import correct
from corner.event import Event
from corner.title_corrections import TITLE_CORRECTIONS


__all__ = ['EventBuilder']


class EventBuilder:
    def __init__(self, directors_builder, row):
        self._directors_builder = directors_builder

        self.id_ = row[0]
        self.title = row[1]
        self.alternative_title = row[2]
        self.year_released = row[3]
        self.certificate = row[4]
        self.directors = row[5]
        self.language = row[6]

        self._build()

    def _build(self):
        self.event = Event(
            self._build_id(),
            self._build_title(),
            self._build_directors(),
            alternative_title=self._build_alternative_title(),
            certificate=self._build_certificate(),
            has_musical_accompaniment=self._build_has_musical_accompaniment(),
            is_live=self._build_is_live(),
            is_preview=self._build_is_preview(),
            is_silent=self._build_is_silent(),
            year_released=self._build_year_released(),
        )

    def _build_id(self):
        return int(self.id_)

    def _build_title(self):
        corrected, title = self._correct_title(self.title)
        self.corrected_title = corrected
        return title

    def _build_alternative_title(self):
        corrected, title = self._correct_title(self.alternative_title)
        self.corrected_alternative_title = corrected
        return title

    def _build_certificate(self):
        if self.certificate in CERTIFICATES:
            return self.certificate

    def _build_directors(self):
        return [director_builder.director for director_builder in
                self._directors_builder.get_director_builders(self.directors)]

    def _build_has_musical_accompaniment(self):
        return self.language == 'Silent w/ musical accompaniment' or \
                self.title == 'The Lodger plus Live Accompaniment'

    def _build_is_live(self):
        return self.certificate == 'live'

    def _build_is_preview(self):
        return 'Preview' in self.title

    def _build_is_silent(self):
        return self.language.startswith('Silent')

    def _build_year_released(self):
        with suppress(ValueError):
            return int(self.year_released)

    def _correct_title(self, title):
        title = title.strip()
        if title:
            if title in TITLE_CORRECTIONS:
                return True, TITLE_CORRECTIONS[title]
            else:
                return correct(title)
        return False, None

