from flask import Blueprint, render_template, url_for, redirect, request, session
from ..models import genres
from ..controllers import movie_controller
import json

blueprint = Blueprint('home', __name__, static_folder='/Users/mgulati/Documents/vscode-projects/sinema/project/static', url_prefix='')

@blueprint.route('/home/', methods=['GET', 'POST'])
def home():
    genre_to_movies = movie_controller.get_movies_by_genre('Action')
    year_to_movies = movie_controller.get_movies_by_year('2018')
    director_to_movies = movie_controller.get_movies_by_actor('Stephen', 'Spielberg')
    actor_to_movies = movie_controller.get_movies_by_actor('Leonardo', 'Dicaprio')
    # writer_to_movies = movie_controller.get_movies_by_writer('Stan', 'Lee')

    session['genre_to_movies'] = [m.serialize() for m in genre_to_movies]
    session['year_to_movies'] = [m.serialize() for m in year_to_movies]
    session['director_to_movies'] = [m.serialize()for m in director_to_movies]
    session['actor_to_movies'] = [m.serialize() for m in actor_to_movies]
    # session['writer_to_movies'] = writer_to_movies

    # if request.method == 'POST':
    #     # genre = request.form.get('Genre')
    #     year = request.form.get('Year')

    #     # genre_to_movies = movie_controller.get_movies_by_genre(genre)
    #     year_to_movies = movie_controller.get_movies_by_year(year)

    return render_template('home.html',
        genres=genres.get_genres(),
        genre_to_movies=genre_to_movies,
        year_to_movies=year_to_movies,
        director_to_movies=director_to_movies,
        actor_to_movies=actor_to_movies
    )

@blueprint.route('/home/genre_lookup/submit/', methods=['POST'])
def genre_lookup():
    if request.method == 'POST':
        genre = request.form.get('Genre')
        genre_to_movies = movie_controller.get_movies_by_genre(genre)

        session['genre_to_movies'] = [m.serialize() for m in genre_to_movies]
    
        return render_template('home.html', 
            genres=genres.get_genres(),
            genre_to_movies=genre_to_movies,
            year_to_movies=ds(session['year_to_movies']),
            director_to_movies=ds(session['director_to_movies']),
            actor_to_movies=ds(session['actor_to_movies'])
        )

@blueprint.route('/home/year_lookup/submit/', methods=['POST'])
def year_lookup():
    if request.method == 'POST':
        year = request.form['Year']
        year_to_movies = movie_controller.get_movies_by_year(year)

        session['year_to_movies'] = [m.serialize() for m in year_to_movies]
    
        return render_template('home.html', 
            genres=genres.get_genres(),
            genre_to_movies=ds(session['genre_to_movies']),
            year_to_movies=year_to_movies,
            director_to_movies=ds(session['director_to_movies']),
            actor_to_movies=ds(session['actor_to_movies'])
        )

def ds(movies):
    return [json.loads(m) for m in movies]

