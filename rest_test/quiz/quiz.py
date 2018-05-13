import uuid
from datetime import datetime

from flask import request, json
from flask_jwt import current_identity
from flask_mail import Message

from rest_test.extensions import mail
from rest_test.quiz.model import Candidate, CandidateStatus
from rest_test.quiz.repo import CandidateRepo
from rest_test.quiz.translations import get_text
from rest_test.user.model import User


def create_new_candidate_token():
    user: User = current_identity
    token = str(uuid.uuid4())
    candidate = Candidate(
        email=request.json.get('email'),
        name=request.json.get('name'),
        created_at=datetime.now(),
        token=token,
        quiz_type=request.json.get('quiz_type'),
        status=str(CandidateStatus.ACTIVE),
        created_by=user.id,
    )
    candidate = CandidateRepo.add(candidate)
    mail.send(Message(
        get_text('candidate_token_mail_subject'),
        recipients=[user.email, candidate.email],
        body=json.dumps({
            'message': get_text('candidate_token_mail_body'),
            'token': token,
        })
    ))
