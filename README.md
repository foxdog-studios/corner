# Corner

Cornerhouse data linked to TheMovieDb

A utility that aims to link together data from that realeased by
[Cornerhouse](http://www.cornerhouse.org/) with
[themoviedb](https://www.themoviedb.org/).

This project was created for the [AND film data
hack](http://www.andfestival.org.uk/blog/and-hack1-datasets/).


## Examples of this data in action

- [fuiz - multiplayer buzzer quiz on films shown at Cornerhouse with automatically generated questions](http://fuiz.fds.com)

## Data

__[Get the data here](https://docs.google.com/spreadsheets/d/12b5_UO5ytTe2jafqzLo8F4V5mnvsx5N47iyUlDK98Tk/edit?usp=sharing)__


### Linking to other data sources

In the `films` data there is the `imdb_id`, which is its id in on
[IMDb](http://www.imdb.com/).

This can be used to link it back to IMDb

    http://www.imdb.com/title/<imdb_id>/

e.g.
[http://www.imdb.com/title/tt0185937/](http://www.imdb.com/title/tt0185937/)

Or to the Rotten Tomatoes API (you will need to [sign up for an API
key](http://developer.rottentomatoes.com/member/register))

    http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json?type=imdb&id=<imdb_id_without_the_tt_prefix>&apikey=<your_api_key>

e.g.[http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json?type=imdb&id=0130827&apikey=<your_api_key>&_prettyprint=true](http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json?type=imdb&id=0130827&apikey=<your_api_key>&_prettyprint=true)


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
  approximately
  [700 events](https://github.com/foxdog-studios/corner/blob/master/corner/events_filter.py)
  that could not be automatically identified and have yet to be manually
  identified.

  * `event_id` The ID of the Cornhouse house event this film was shown during.
    This links `films` to `events`.

  * `tmdb_film_id` The ID of the film on TMDb. To access the movie via TMDb's
    API, use the URL
    `https://api.themoviedb.org/3/movie/<tmdb_film_id>?api_key=<api_key>`,
    substiting `<tmdb_film_id>` and `<api_key>`.

  * `title`: The film's English title. This may not be the original title (see
    the `original_title` field.

  * `adult`: `0` if the film is pornographic and `1` if not.

  * `backdrop_path` (Optional): The file path of the film's backdrop image. To
    retreive the image, see the "TMDb image URLs" section below.

  * `budget` (Optional): The film's budget in American dollars. It appears that
    the budgets have _not_ been adjusted for inflation.

  * `homepage` (Optional): The URL of the website associated with the film. The
    website's of many older films no longer exist.

  * `imdb_id` (Optional): The IMDb ID for this film. To retrieve the IMDb
    listing, use the URL `http://www.imdb.com/title/<imdb_id>/`, substituting
    `<imdb_id>`.

  * `original_title`: The film's original title, this may not be in English.

  * `Overview` (Optional): A short description of the film in English.

  * `popularity`: ?

  * `poster_path` (Optional): The file path of the film's poster image. To
    retrieve the image, see the "TMDb image URLs" section below.

  * `release_date` (Optional): The date the film was released. I'm not sure if
    this is the original release date or the UK release date.

  * `revenue` (Optional):

  * `runtime (Optional):

  * `status`:

  * `tagline` (Optional):

  * `vote_average`:

  * `vote_count`:


### TMDb image URLs

To build an image URL, you will need 3 pieces of data. The `base_url`, `size`
and `file_path`. Simply combine them all and you will have a fully qualified
URL. Here’s an example URL:

    http://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg


## Data sources

- [Cornerhouse films screened since Nov
  1999](http://www.andfestival.org.uk/wp-content/uploads/2014/06/Cornerhouse-films-screened-since-Nov-1999.csv)

- [themoviedb API](http://docs.themoviedb.apiary.io/)

