__all__ = ['Director']


class Director:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Director({!r})'.format(self.name)

