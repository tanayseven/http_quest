from typing import Union

from http_quiz.ext import db
from http_quiz.quiz.model import Candidate


class CandidateRepo:
    @staticmethod
    def add(candidate: Candidate) -> Candidate:
        db.session.add(candidate)
        db.session.commit()
        return candidate

    @staticmethod
    def fetch_candidate_by_token(token: str) -> Union[Candidate, None]:
        return db.session.query(Candidate).\
            filter(Candidate.token == token).one_or_none()

