from flask import Blueprint, jsonify
from flask_jwt import jwt_required

from http_quest.quiz.model import QuizType
from http_quest.quiz.quiz import create_new_candidate_token
from http_quest.quiz.schema import new_candidate_token_schema
from http_quest.quiz.translations import get_text
from http_quest.utilities import validate_json

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


@quiz_view.route('/quiz/list_quiz_types', methods=('GET',))
@jwt_required()
def list_quiz_types():
    response = {
        'list_quiz_types': [str(type_) for type_ in QuizType]
    }
    return jsonify(response), 200
