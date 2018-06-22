from enum import Enum

from sqlalchemy.dialects.postgresql import JSONB

from http_quiz.ext import db


class CandidateStatus(Enum):
    ACTIVE = 'active'
    EXPIRED = 'expired'

    def __str__(self) -> str:
        return self.value


class QuestionStatus(Enum):
    PENDING = 'pending'
    CORRECT = 'correct'
    WRONG = 'wrong'
    TIME_EXPIRED = 'time_expired'

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
    quiz_name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(64))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))


class SequentialQuiz(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'))
    problem_number = db.Column(db.Integer)
    input = db.Column(JSONB)
    output = db.Column(JSONB)
    attempts = db.Column(db.Integer, default=1)
    status = db.Column(db.String(64))

    def pending_or_wrong(self, problem_no: int) -> bool:
        return self.problem_number == problem_no \
               and (self.status == str(QuestionStatus.PENDING) or self.status == str(QuestionStatus.WRONG))

    def has_been_solved(self, problem_no: int) -> bool:
        return self.problem_number == problem_no and self.status == str(QuestionStatus.CORRECT)
