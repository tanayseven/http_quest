import uuid
from datetime import datetime
from functools import wraps

from flask import request, jsonify, url_for, g
from flask_jwt import current_identity
from flask_mail import Message

from http_quiz.ext import mail
from http_quiz.quiz.model import Candidate, CandidateStatus
from http_quiz.quiz.repo import CandidateRepo
from http_quiz.quiz.translations import get_text
from http_quiz.user.model import User
from http_quiz.utilities import load_template


def create_new_candidate_token():
    user: User = current_identity
    token = str(uuid.uuid4())
    candidate = Candidate(
        email=request.json.get('email'),
        name=request.json.get('name'),
        created_at=datetime.now(),
        token=token,
        quiz_type=request.json.get('quiz_type'),
        quiz_name=request.json.get('quiz_name'),
        status=str(CandidateStatus.ACTIVE),
        created_by=user.id,
    )
    candidate = CandidateRepo.add(candidate)
    mail.send(Message(
        get_text('candidate_token_mail_subject'),
        recipients=[user.email, candidate.email],
        body=load_template('candidate_token.html', {
            'token': token,
            'candidate_name': candidate.name,
            'quiz_url': url_for(candidate.quiz_name + '_quiz.problem_statement'),
        }),
    ))


def candidate_token_required(quiz_type: str, quiz_name: str):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            candidate = CandidateRepo.fetch_candidate_by_token(request.headers.get('Authorization'))
            if candidate.quiz_type == quiz_type and candidate.quiz_name == quiz_name:
                g.candidate = candidate
                return f(*args, **kwargs)
            return jsonify({'message': 'Invalid Authorization Token'}), 401

        return decorated_function

    return decorator
