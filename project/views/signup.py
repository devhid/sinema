from flask import Blueprint, render_template

blueprint = Blueprint('signup', __name__, static_folder='../static')

@blueprint.route('/')
def signup():
    return render_template('signup.html')
