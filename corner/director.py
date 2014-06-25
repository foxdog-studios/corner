__all__ = ['Director']


class Director:
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

    def __repr__(self):
        return 'Director({!r}, {!r})'.format(self.id_, self.name)

    def __str__(self):
        return self.name

