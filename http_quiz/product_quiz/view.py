from flask import Blueprint, jsonify

from http_quiz.quiz.quiz import candidate_token_required

products_view = Blueprint('product_quiz', __name__)


@products_view.route('/product_quiz/')
def root():
    data = {'message': 'You are at the root of all the endpoints. Please go to /product_quiz/problem_statement/ '
                       'for the first problem'}
    return jsonify(data)


@products_view.route('/product_quiz/problem_statement', methods=('GET',))
@candidate_token_required('sequential', 'product_quiz')
def problem_statement():
    pass
