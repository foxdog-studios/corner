# Corner

Cornerhouse data linked to TheMovieDb

A utility that aims to link together data from that realeased by
[Cornerhouse](http://www.cornerhouse.org/) with
[themoviedb](https://www.themoviedb.org/).

This project was created for the [AND film data
hack](http://www.andfestival.org.uk/blog/and-hack1-datasets/).


## Data

__[Get the data here](https://docs.google.com/spreadsheets/d/12b5_UO5ytTe2jafqzLo8F4V5mnvsx5N47iyUlDK98Tk/edit?usp=sharing)__


### Data structure

* `events` The film related events hosted by the Cornerhouse since 1999.

  * `event_id` The ID of an event assigned by Cornerhouse.

  * `title` An event's title, may or may not be English.

  * `alternative_title` (Optional) An alternative title for an event. Normally
     a translation to English if `title` is in English, or the original title
     if `title` is the translation.

  * `release_year` (Optional) The year the content of the event was released in
    YYYY format.

  * `certificate` (Optional) An event's age certificate. One of `U`, `PG`,
    `12A`, `12`, `15`, `18`.

  * `languages` (Optional) Unstructured information about languages used in the
    content of an event. This includes spoken languages, dubbed languages,
    subtitle languages, and whether the event contains silent films and, if so,
    whether there is live accompaniment. For structures language information,
    see `spoken_languages.csv`.

  * `duration` (Optional) The runtime of an event in minutes (> 0).

  * `country_of_origin` (Optional) Unstructured information about the countries
    involved in the creation of the content in an event.

  * `actors` (Optional) Unstructured information about the actors featured
    in the content in an event.


* `films` Films show during Cornhouse events since 1999. Excludes the films from
  approximately 700 events that could not be automatically identified and have
  yet to be manually identified.

  * `event_id` The ID of the Cornhouse house event this film was shown during.
    This links `films` to `events`.

  * `tmdb_film_id` The ID of the film on TMDb. To access the movie via TMDb's
    API, use the URL
    `https://api.themoviedb.org/3/movie/<tmdb_film_id>?api_key=<api_key>`,
    substiting `<tmdb_film_id>` and `<api_key>`.

  *  `adult`: If the film is pornographic, `0`, else `1`.


## Data sources

- [Cornerhouse films screened since Nov
  1999](http://www.andfestival.org.uk/wp-content/uploads/2014/06/Cornerhouse-films-screened-since-Nov-1999.csv)

- [themoviedb API](http://docs.themoviedb.apiary.io/)

