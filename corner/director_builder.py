from corner.character_corrections import correct
from corner.director import Director


class DirectorBuilder:
    def __init__(self, name):
        self.name = name
        self.director = Director(self._build_name())

    def _build_name(self):
        self.corrected_name, name = correct(self.name)
        return name

