from flask import Blueprint, render_template

blueprint = Blueprint('index', __name__, static_url_path='')

@blueprint.route('/')
def index():
    return render_template('index.html')