from flask import Blueprint, jsonify

products_view = Blueprint('product', __name__)


@products_view.route('/product/')
def root():
    data = {'message': 'You are at the root of all the endpoints'}
    return jsonify(data)
