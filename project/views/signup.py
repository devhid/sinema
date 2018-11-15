from flask import Blueprint, render_template

blueprint = Blueprint('signup', __name__, static_url_path='')

@blueprint.route('/signup')
def signup():
    return render_template('signup.html')