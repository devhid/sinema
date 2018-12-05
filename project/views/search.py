import json
from flask import Blueprint, render_template, url_for, redirect, request, g, flash

from ..controllers import person_controller, genre_controller, movie_controller
from ..forms import SearchForm
from ..models import movie

blueprint = Blueprint('search', __name__, static_folder='/Users/mgulati/Documents/vscode-projects/sinema/project/static', url_prefix='')

@blueprint.route('/search/', methods=['GET', 'POST'])
def search():
    if not g.search_form.validate():
        return redirect(url_for('home.home'))
    movies, total = movie_controller.get_movies_by_keywords(g.search_form.q.data)
    
    movie_list = []
    for m_movie in movies:
        m_movie.maturity_rating = movie_controller.strip_enum(m_movie.maturity_rating)
        movie_list.append(m_movie)

    return render_template('search.html', 
        movie_groups=chunks(movie_list, 5),
        get_actors_by_movie=person_controller.get_actors_by_movie,
        get_directors_by_movie=person_controller.get_directors_by_movie,
        get_writers_by_movie=person_controller.get_writers_by_movie,
        get_genres_by_movie=genre_controller.get_genres_by_movie
    )

@blueprint.before_app_request
def before_request():
    g.search_form = SearchForm()

def chunks(L, n):
    """ Yield successive n-sized chunks from L.
    """
    chunks = []
    for i in range(0, len(L), n):
        chunks.append(L[i:i+n])

    return chunks