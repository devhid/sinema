from flask import Blueprint, render_template, url_for, redirect

blueprint = Blueprint('home', __name__, static_folder='../static')


@blueprint.route('/home/')
def home():
    return redirect(url_for('home.browse'))

@blueprint.route('/home/browse')
def browse():
    return render_template('home.html')
