from sqlalchemy import extract
from ..models import movie, genres, person, actors, writers, directors

def get_movies_by_keywords(keywords):
    return movie.Movie.search(keywords, 1, 200)

def get_movies_by_actor(first_name, last_name):
    persons = person.Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = set()
    for m_person in persons:
        actor_to_movie = actors.Actors.query.filter_by(actor_id=m_person.person_id).all()

        for mapping in actor_to_movie:
            m_movie = movie.Movie.query.get(mapping.movie_id)
            m_movie.maturity_rating = strip_enum(m_movie.maturity_rating)

            if m_movie:
                movies.add(m_movie)
    
    return movies

def get_movies_by_director(first_name, last_name):
    persons = person.Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = set()
    for m_person in persons:
        director_to_movie = directors.Directors.query.filter_by(director_id=m_person.person_id).all()

        for mapping in director_to_movie:
            m_movie = movie.Movie.query.get(mapping.movie_id)
            m_movie.maturity_rating = strip_enum(m_movie.maturity_rating)

            if m_movie:
                movies.add(m_movie)
    
    return movies

def get_movies_by_writer(first_name, last_name):
    persons = person.Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = set()
    for m_person in persons:
        writer_to_movie = writers.Writers.query.filter_by(writer_id=m_person.person_id).all()

        for mapping in writer_to_movie:
            m_movie = movie.Movie.query.get(mapping.movie_id)
            m_movie.maturity_rating = strip_enum(m_movie.maturity_rating)

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
            m_movie.maturity_rating = strip_enum(m_movie.maturity_rating)
            movies.add(m_movie)

    return movies

def get_movies_by_year(year):
    movies = movie.Movie.query.filter(extract('year', movie.Movie.release_date) == year).all()

    for m_movie in movies:
        m_movie.maturity_rating = strip_enum(m_movie.maturity_rating)
    
    return set(movies)

def get_movies_by_rating(rating):
    return set(movie.Movie.query.filter(movie.Movie.rating >= rating).all())


def strip_enum(enum_member):
    return str(enum_member).replace('MaturityRating.', '')

