__all__ = ['Event']


class Event:
    def __init__(
            self,
            id_,
            title,
            directors,
            alternative_title=None,
            certificate=None,
            is_live=False,
            is_preview=False,
            is_silent=False,
            year_released=None
        ):
        self.id_ = id_
        self.title = title
        self.directors = directors
        self.alternative_title = alternative_title
        self.certificate = certificate
        self.is_live = is_live
        self.is_preview = is_preview
        self.is_silent = is_silent
        self.year_released = year_released

