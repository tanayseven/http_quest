from flask import Blueprint, jsonify
from flask_jwt import jwt_required

from rest_test.quiz.quiz import create_new_candidate_token
from rest_test.quiz.schema import new_candidate_token_schema
from rest_test.quiz.translations import get_text
from rest_test.utilities import validate_json

quiz_view = Blueprint('quiz', __name__)


@quiz_view.route('/quiz/new_candidate_token', methods=('POST',))
@validate_json(new_candidate_token_schema)
@jwt_required()
def create_candidate_token():
    response = {
        'message': get_text('candidate_token_success')
    }
    create_new_candidate_token()
    return jsonify(response), 200
