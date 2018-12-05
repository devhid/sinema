from flask import Blueprint, render_template, url_for, redirect, request, session
from ..models import movie
from ..controllers import movie_controller
import json

blueprint = Blueprint('movie_info', __name__, static_folder='/Users/mgulati/Documents/vscode-projects/sinema/project/static', url_prefix='')

@blueprint.route('/movie/<int:movie_id>/', methods=['GET', 'POST'])
def movie_info(movie_id):
    m_movie = movie.Movie.query.get(movie_id)
    if not m_movie:
        return render_template('404.html')

    return render_template('movie_info.html', movie=m_movie)