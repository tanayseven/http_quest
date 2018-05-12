from flask import Blueprint, jsonify

from rest_test.translations import get_text

root_view = Blueprint('root', __name__)


@root_view.route('/', methods=('GET',))
def root_get():
    data = {'message': get_text('root_welcome')}
    return jsonify(data)
