from flask import Blueprint, render_template, url_for, redirect

blueprint = Blueprint('new_releases', __name__, static_folder='../static')

@blueprint.route('/new_releases/')
def recently_added():
    return render_template('new_releases.html')