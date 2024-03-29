from flask import Flask, render_template
from elasticsearch import Elasticsearch
import os

from .extensions import db
from .views import home, signup, index, recently_added, new_releases, movie_info, search
from .models import movie, person, actors, writers, directors, genres
from .movie_data import get_movie_info
from .controllers import movie_controller
from .database import *

def create_app(config_file):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """

    app = Flask(__name__.split('.')[0])
    app.config.from_pyfile(config_file)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""
    with app.app_context():
        db.init_app(app)
        app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
            if app.config['ELASTICSEARCH_URL'] else None

        # db.create_all()
        # populate_database(db)

        # movie.Movie.reindex()
        # query, total = movie.Movie.search('Iron', 1, 100)
        # print(total)
        # print(query.all())

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home.blueprint)
    app.register_blueprint(signup.blueprint)
    app.register_blueprint(index.blueprint)
    app.register_blueprint(recently_added.blueprint)
    app.register_blueprint(new_releases.blueprint)
    app.register_blueprint(movie_info.blueprint)
    app.register_blueprint(search.blueprint)

def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'Person': person,
            'Movie': movie,
            'Actors': actors,
            'Writers': writers,
            'Directors': directors,
            'Genres': genres
        }

    app.shell_context_processor(shell_context)