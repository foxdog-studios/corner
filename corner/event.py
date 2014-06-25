__all__ = ['Event']


class Event:
    def __init__(
            self,
            id_,
            title,
            directors,
            alternative_title=None,
            certificate=None,
            is_preview=False,
            is_live=False,
            year=None
        ):
        self.id_ = id_
        self.title = title
        self.directors = directors
        self.alternative_title = alternative_title
        self.certificate = certificate
        self.is_preview = is_preview
        self.is_live = is_live
        self.year = year

