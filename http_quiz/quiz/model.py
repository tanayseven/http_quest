from enum import Enum

from http_quiz.extensions import db


class CandidateStatus(Enum):
    ACTIVE = 'active'
    EXPIRED = 'expired'

    def __str__(self) -> str:
        return self.value


class QuizType(Enum):
    SEQUENTIAL = 'sequential'

    def __str__(self) -> str:
        return self.value


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255))
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    token = db.Column(db.String(255), unique=True)
    quiz_type = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(64))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
