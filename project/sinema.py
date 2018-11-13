from flask import Flask, render_template
from .extensions import db
from .views import home, signup

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
    db.init_app(app)

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home.blueprint)
    app.register_blueprint(signup.blueprint)

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