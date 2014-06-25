from corner.director import Director


class DirectorBuilder:
    def __init__(self, name):
        self.name = name
        self.director = Director(name)

