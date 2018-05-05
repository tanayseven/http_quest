from flask import Blueprint, jsonify

root_view = Blueprint('root', __name__)


@root_view.route('/', methods=('GET',))
def root_get():
    data = {'message': 'this is the / please go to /login for any further activity'}
    return jsonify(data)
