from flask import Blueprint, render_template, url_for, redirect

blueprint = Blueprint('home', __name__, static_folder='../static')

@blueprint.route('/home/')
def home():
    return render_template('home.html')