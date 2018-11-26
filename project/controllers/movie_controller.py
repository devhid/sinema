from sqlalchemy import extract
from ..extensions import db
from ..models import movie, genres, person, actors

def get_movies_by_name(name):
    pass
    # return Movie.search(name)
    # TODO: Get a lot of movie data to work with for each genre and actor/director/producer relationships.
    # TODO: Implement search indexing for this function.

def get_movies_by_actor(first_name, last_name):
    persons = person.Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = set()
    for m_person in persons:
        actor_to_movie = actors.Actors.query.filter_by(actor_id=m_person.person_id).all()

        for mapping in actor_to_movie:
            m_movie = movie.Movie.query.get(mapping.movie_id)

            if m_movie:
                movies.add(m_movie)
    
    return movies

def get_movies_by_director(first_name, last_name):
    persons = person.Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = set()
    for m_person in persons:
        director_to_movie = directors.Directors.query.filter_by(director_id=m_person.person_id).all()

        for mapping in director_to_movie:
            m_movie = movie.Movie.query.get(movie_id=mapping.movie_id)

            if m_movie:
                movies.add(m_movie)
    
    return movies

def get_movies_by_writer(first_name, last_name):
    persons = person.Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = set()
    for m_person in persons:
        writer_to_movie = writers.Writers.query.filter_by(writer_id=m_person.person_id).all()

        for mapping in writer_to_movie:
            m_movie = movie.Movie.query.get(movie_id=mapping.movie_id)

            if m_movie:
                movies.add(m_movie)
    
    return movies

def get_movies_by_genre(genre):
    genre_to_movie = genres.Genres.query.filter_by(genre=genre).all()

    movies = set()
    for mapping in genre_to_movie:

        movie_id = mapping.movie_id
        m_movie = movie.Movie.query.get(movie_id)

        if m_movie:
            movies.add(m_movie)

    return movies

def get_movies_by_year(year):
    return movie.Movie.query.filter(extract('year', movie.Movie.release_date) == year).all()

