from flask import Blueprint, jsonify

products_view = Blueprint('product', __name__)


@products_view.route('/product/')
def root():
    data = {'root': 'you are at the root of the endpoints'}
    return jsonify(data)
