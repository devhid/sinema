from sqlalchemy import extract
from ..extensions import db
from ..models import movie.Movie, genres.Genres, person.Person, actors.Actors

def get_movies_by_name(name):
    # return Movie.search(name)

def get_movies_by_actor(first_name, last_name):
    persons = Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = []
    for person in persons:
        actor_to_movie = Actor.query.filter_by(actor_id=person.actor_id).all()

        for mapping in actor_to_movie:
            movie = Movie.query.get(movie_id=mapping.movie_id)

            if movie:
                movies.append(movie)
    
    return movies

def get_movies_by_director(first_name, last_name):
    persons = Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = []
    for person in persons:
        director_to_movie = Director.query.filter_by(director_id=person.director_id).all()

        for mapping in director_to_movie:
            movie = Movie.query.get(movie_id=mapping.movie_id)

            if movie:
                movies.append(movie)
    
    return movies

def get_movies_by_producer(first_name, last_name):
    persons = Person.query.filter_by(first_name=first_name, last_name=last_name).all()

    movies = []
    for person in persons:
        producer_to_movie = Producer.query.filter_by(producer_id=person.producer_id).all()

        for mapping in producer_to_movie:
            movie = Movie.query.get(movie_id=mapping.movie_id)

            if movie:
                movies.append(movie)
    
    return movies

def get_movies_by_genre(genre):
    genre_to_movie = Genres.query.filter_by(genre=genre).all()

    movies = []
    for mapping in genre_to_movie:

        movie_id = mapping.movie_id
        movie = Movies.query.get(movie_id)

        if movie:
            movies.append(movie)

    return movies

def get_movies_by_year(year):
    return Movie.query.filter_by(extract('year'), Movie.release_date) == year).all()

