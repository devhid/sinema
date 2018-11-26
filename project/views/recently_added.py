from flask import Blueprint, render_template, url_for, redirect

blueprint = Blueprint('recently_added', __name__, static_folder='../static')

@blueprint.route('/recently_added/')
def recently_added():
    return render_template('recently_added.html')