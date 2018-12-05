import json
from flask import Blueprint, render_template, url_for, redirect, request, session, make_response, g

from ..models import genres
from ..controllers import movie_controller, person_controller, genre_controller
from ..movie_data import get_movie_info
from ..database import populate_database

blueprint = Blueprint('home', __name__, static_folder='/Users/mgulati/Documents/vscode-projects/sinema/project/static', url_prefix='')

@blueprint.route('/home/', methods=['GET', 'POST'])
def home():
    genre_to_movies = movie_controller.get_movies_by_genre('Action')
    year_to_movies = movie_controller.get_movies_by_year('2016')
    rating_to_movies = movie_controller.get_movies_by_rating(2.0)
    director_to_movies = movie_controller.get_movies_by_director('James', 'Cameron')
    actor_to_movies = movie_controller.get_movies_by_actor('Tom', 'Cruise')
    writer_to_movies = movie_controller.get_movies_by_writer('Quentin', 'Tarantino')

    # session['genre_to_movies'] = [m.serialize() for m in genre_to_movies]
    # session['year_to_movies'] = [m.serialize() for m in year_to_movies]
    # session['director_to_movies'] = [m.serialize()for m in director_to_movies]
    # session['actor_to_movies'] = [m.serialize() for m in actor_to_movies]
    # session['writer_to_movies'] = [m.serialize() for m in writer_to_movies]

    return render_template('home.html',
        genres=genres.get_genres(),
        genre_to_movies=genre_to_movies,
        year_to_movies=year_to_movies,
        rating_to_movies=rating_to_movies,
        director_to_movies=director_to_movies,
        actor_to_movies=actor_to_movies,
        writer_to_movies=writer_to_movies,
        get_actors_by_movie=person_controller.get_actors_by_movie,
        get_directors_by_movie=person_controller.get_directors_by_movie,
        get_writers_by_movie=person_controller.get_writers_by_movie,
        get_genres_by_movie=genre_controller.get_genres_by_movie,
    )

@blueprint.route('/home/search_genre/submit/', methods=['POST'])
def search_genre():
    if request.method == 'POST':
        genre = request.form.get('genre')
        genre_to_movies = movie_controller.get_movies_by_genre(genre)

        # session['genre_to_movies'] = [m.serialize() for m in genre_to_movies]
    
        return render_template('home.html', 
            genres=genres.get_genres(),
            genre_to_movies=genre_to_movies,
            get_actors_by_movie=person_controller.get_actors_by_movie,
            get_directors_by_movie=person_controller.get_directors_by_movie,
            get_writers_by_movie=person_controller.get_writers_by_movie,
            get_genres_by_movie=genre_controller.get_genres_by_movie
            # year_to_movies=ds(session['year_to_movies']),
            # director_to_movies=ds(session['director_to_movies']),
            # actor_to_movies=ds(session['actor_to_movies']),
            # writer_to_movies=ds(session['writer_to_movies'])
        )

@blueprint.route('/home/search_year/submit/', methods=['POST'])
def search_year():
    if request.method == 'POST':
        year = request.form['year']
        year_to_movies = movie_controller.get_movies_by_year(year)

        # session['year_to_movies'] = [m.serialize() for m in year_to_movies]
    
        return render_template('home.html', 
            genres=genres.get_genres(),
            year_to_movies=year_to_movies,
            get_actors_by_movie=person_controller.get_actors_by_movie,
            get_directors_by_movie=person_controller.get_directors_by_movie,
            get_writers_by_movie=person_controller.get_writers_by_movie,
            get_genres_by_movie=genre_controller.get_genres_by_movie
            # genre_to_movies=ds(session['genre_to_movies']),
            # director_to_movies=ds(session['director_to_movies']),
            # actor_to_movies=ds(session['actor_to_movies']),
            # writer_to_movies=ds(session['writer_to_movies'])
        )

@blueprint.route('/home/search_rating/submit/', methods=['POST'])
def search_rating():
    if request.method == 'POST':
        rating = request.form['rating']
        rating_to_movies = movie_controller.get_movies_by_rating(rating)

        # session['rating_to_movies'] = [m.serialize() for m in year_to_movies]
    
        return render_template('home.html', 
            genres=genres.get_genres(),
            rating_to_movies=rating_to_movies,
            get_actors_by_movie=person_controller.get_actors_by_movie,
            get_directors_by_movie=person_controller.get_directors_by_movie,
            get_writers_by_movie=person_controller.get_writers_by_movie,
            get_genres_by_movie=genre_controller.get_genres_by_movie
            # genre_to_movies=ds(session['genre_to_movies']),
            # year_to_movies=ds(session['year_to_movies']),
            # director_to_movies=ds(session['director_to_movies']),
            # actor_to_movies=ds(session['actor_to_movies']),
            # writer_to_movies=ds(session['writer_to_movies'])
        )

@blueprint.route('/home/search_actor/submit/', methods=['POST'])
def search_actor():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        actor_to_movies = movie_controller.get_movies_by_actor(first_name, last_name)

        # session['actor_to_movies'] = [m.serialize() for m in actor_to_movies]

        return render_template('home.html', 
            genres=genres.get_genres(),
            actor_to_movies=actor_to_movies,
            get_actors_by_movie=person_controller.get_actors_by_movie,
            get_directors_by_movie=person_controller.get_directors_by_movie,
            get_writers_by_movie=person_controller.get_writers_by_movie,
            get_genres_by_movie=genre_controller.get_genres_by_movie
            # genre_to_movies=ds(session['genre_to_movies']),
            # year_to_movies=ds(session['year_to_movies']),
            # director_to_movies=ds(session['director_to_movies']),
            # writer_to_movies=ds(session['writer_to_movies'])
        )

@blueprint.route('/home/search_director/submit/', methods=['POST'])
def search_director():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        director_to_movies = movie_controller.get_movies_by_director(first_name, last_name)

        # session['director_to_movies'] = [m.serialize() for m in director_to_movies]

        return render_template('home.html', 
            genres=genres.get_genres(),
            director_to_movies=director_to_movies,
            get_actors_by_movie=person_controller.get_actors_by_movie,
            get_directors_by_movie=person_controller.get_directors_by_movie,
            get_writers_by_movie=person_controller.get_writers_by_movie,
            get_genres_by_movie=genre_controller.get_genres_by_movie
            # genre_to_movies=ds(session['genre_to_movies']),
            # year_to_movies=ds(session['year_to_movies']),
            # actor_to_movies=ds(session['actor_to_movies']),
            # writer_to_movies=ds(session['writer_to_movies'])
        )

@blueprint.route('/home/search_writer/submit/', methods=['POST'])
def search_writer():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        writer_to_movies = movie_controller.get_movies_by_writer(first_name, last_name)

        # session['writer_to_movies'] = [m.serialize() for m in writer_to_movies]

        return render_template('home.html', 
            genres=genres.get_genres(),
            writer_to_movies=writer_to_movies,
            get_actors_by_movie=person_controller.get_actors_by_movie,
            get_directors_by_movie=person_controller.get_directors_by_movie,
            get_writers_by_movie=person_controller.get_writers_by_movie,
            get_genres_by_movie=genre_controller.get_genres_by_movie
            # genre_to_movies=ds(session['genre_to_movies']),
            # year_to_movies=ds(session['year_to_movies']),
            # director_to_movies=ds(session['director_to_movies']),
            # actor_to_movies=ds(session['actor_to_movies']),
        )

def ds(movies):
    return [json.loads(m) for m in movies]

