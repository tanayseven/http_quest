import uuid
from datetime import datetime

from flask import Blueprint, jsonify, request, json
from flask_jwt import jwt_required, current_identity
from flask_mail import Message

from rest_test.extensions import mail
from rest_test.quiz.model import Candidate, CandidateStatus
from rest_test.quiz.repo import CandidateRepo
from rest_test.quiz.schema import new_candidate_token_schema
from rest_test.quiz.translations import get_text
from rest_test.user.model import User
from rest_test.utilities import validate_json

quiz_view = Blueprint('quiz', __name__)


@quiz_view.route('/quiz/new_candidate_token', methods=('POST',))
@validate_json(new_candidate_token_schema)
@jwt_required()
def create_candidate_token():
    response = {
        'message': get_text('candidate_token_success')
    }
    user: User = current_identity
    token = str(uuid.uuid4())
    candidate = Candidate(
        email=request.json.get('email'),
        name=request.json.get('name'),
        created_at=datetime.now(),
        token=token,
        status=str(CandidateStatus.ACTIVE),
        created_by=user.id,
    )
    candidate = CandidateRepo.add(candidate)
    mail.send(Message(
        get_text('candidate_token_mail_subject'),
        recipients=[user.email, candidate.email],
        body=json.dumps({
            'message': get_text('Use the following token as an HTTP header called `Authorization`'),
            'token': token,
        })
    ))
    return jsonify(response), 200
