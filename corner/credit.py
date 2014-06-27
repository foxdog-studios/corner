class Credit:
    def __init__(self, film, credit, person):
        self.film = film
        self.credit = credit
        self.person = person

        self.tmdb_film_id = self.film.tmdb_film_id
        self.tmdb_person_id = self.person.tmdb_person_id

