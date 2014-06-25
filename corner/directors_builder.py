from corner.director_builder import DirectorBuilder


__all__ = ['DirectorsBuilder']


class DirectorsBuilder:
    def __init__(self, rows):
        self._by_name = {}
        self.directors = []
        self.director_builders = []

        names = set()
        for row in rows:
            names.update(self.split(row[5]))

        for name in names:
            director_builder = DirectorBuilder(name)
            self._by_name[name] = director_builder
            self.directors.append(director_builder.director)
            self.director_builders.append(director_builder)

    def get_director_builders(self, text):
       return [self._by_name[name] for name in self.split(text)]

    @staticmethod
    def split(text):
        directors = []
        for director in text.split(', '):
            director = director.strip()
            if director:
                directors.append(director)
        return directors

