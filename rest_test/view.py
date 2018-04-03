from flask import Blueprint, jsonify

root_view = Blueprint('root', __name__)


@root_view.route('/', methods=('GET',))
def something():
    data = {'something': 'the data'}
    return jsonify(data)


@root_view.route('/send', methods=('POST',))
def something_else():
    data = {'something': 'something extra'}
    return jsonify(data)
