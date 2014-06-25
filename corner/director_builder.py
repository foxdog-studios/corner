from itertools import count

from corner.director import Director


class DirectorBuilder:
    _next_id = count()

    def __init__(self, name):
        self.name = name
        self.director = Director(
            self._build_id(),
            self._build_name(),
        )

    def _build_id(self):
        return next(self._next_id)

    def _build_name(self):
        return self.name

