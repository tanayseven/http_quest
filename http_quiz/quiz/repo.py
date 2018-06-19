from typing import Union

from sqlalchemy import desc

from http_quiz.ext import db
from http_quiz.quiz.model import Candidate, SequentialQuiz


class CandidateRepo:
    @staticmethod
    def add(candidate: Candidate) -> Candidate:
        db.session.add(candidate)
        db.session.commit()
        return candidate

    @staticmethod
    def fetch_candidate_by_token(token: str) -> Union[Candidate, None]:
        return db.session.query(Candidate).filter(Candidate.token == token).one_or_none()


class QuizRepo:
    @staticmethod
    def fetch_latest_answer_by_candidate(candidate: Candidate) -> SequentialQuiz:
        return db.session.query(Candidate).join(SequentialQuiz).filter(Candidate.id == candidate.id).order_by(
            desc(SequentialQuiz.problem_number)
        ).limit(1).one_or_none()
