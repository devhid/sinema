from flask import Flask, render_template

from .extensions import db
from .views import home, signup, index, recently_added, new_releases
from .models import movie, person, actors, writers, directors, genres
from .movie_data import get_movie_info
from .controllers import movie_controller

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

        # for m in movie_controller.get_movies_by_year('2018'):
        #     print(str(m.movie_name) + '\n')
        # print("=============================================")

        # for m in movie_controller.get_movies_by_actor('Leonardo', 'Dicaprio'):
        #     print(str(m.movie_name) + '\n')
        # print("=============================================")
        
        # for m in movie_controller.get_movies_by_genre('Horror'):
        #     print(str(m.movie_name) + '\n')
        # print("=============================================")

        # db.create_all()
        # push_db_data()

def push_db_data():
    imdb_ids = "tt0108052,tt0083866,tt0082971,tt3778644,tt3748528,\
                tt0319343,tt1386588,tt0838283,tt1772341,tt0371746,\
                tt1228705,tt1300854,tt0443453,tt2582846,tt0989757,\
                tt1099212,tt1702439,tt0468569,tt1375666,tt0172495,\
                tt0120815,tt1345836,tt0133093,tt0499549,tt0988045,\
                tt5215952,tt0289043,tt1139797,tt5700672,tt1457767,\
                tt6644200,tt3235888,tt1591095".split(',')
    
    for _id in imdb_ids:
        if not get_movie_info(imdbid=_id):
            continue

        title, synopsis, release_date, rating, maturity_rating, duration, _genres, director, _actors, _writers, movie_art_url = get_movie_info(imdbid=_id)
        new_movie = movie.Movie(
            movie_name=title,
            synopsis=synopsis,
            rating=rating,
            minutes_duration=duration,
            release_date=release_date,
            maturity_rating=maturity_rating,
            movie_art_url=movie_art_url
        )
        db.session.add(new_movie)
        db.session.commit()

        for genre in _genres:
            if validate_genre(genre):
                db.session.add(genres.Genres(
                    movie_id=new_movie.movie_id,
                    genre=genre
                ))
                db.session.commit()
        
        for actor in _actors:
            _person = person.Person(
                first_name=actor[0],
                last_name=actor[1]
            )

            db.session.add(_person)
            db.session.commit()

            db.session.add(actors.Actors(
                actor_id=_person.person_id,
                movie_id=new_movie.movie_id
            ))
            db.session.commit()
        
        for writer in _writers:
            _person = person.Person(
                first_name=writer[0],
                last_name=writer[1]
            )

            db.session.add(_person)
            db.session.commit()

            db.session.add(writers.Writers(
                writer_id=_person.person_id,
                movie_id=new_movie.movie_id
            ))
            db.session.commit()

        _person = person.Person(
            first_name=director[0],
            last_name=director[1]
        )

        db.session.add(_person)
        db.session.commit()

        db.session.add(directors.Directors(
            director_id=_person.person_id,
            movie_id=new_movie.movie_id
        ))

        db.session.commit()

def validate_genre(genre):
    return genre in list(genres.Genre.__members__.keys())

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home.blueprint)
    app.register_blueprint(signup.blueprint)
    app.register_blueprint(index.blueprint)
    app.register_blueprint(recently_added.blueprint)
    app.register_blueprint(new_releases.blueprint)

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