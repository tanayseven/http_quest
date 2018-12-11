from flask import Blueprint, jsonify
from flask.templating import render_template

from http_quest.translations import get_text


root_view = Blueprint('root', __name__)


@root_view.route('/', methods=('GET',))
def root_get():
    data = {'message': get_text('root_welcome')}
    return jsonify(data)

@root_view.route('/admin/', methods=('GET',))
def admin_get_index():
    return render_template('/admin/index.html')

@root_view.route('/admin/<path:url_path>', methods=('GET',))
def admin_get(url_path):
    return render_template('/admin/' + url_path)
