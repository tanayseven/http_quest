from typing import Union

from rest_test.extensions import db
from rest_test.quiz.model import Candidate


class CandidateRepo:
    @staticmethod
    def add(candidate: Candidate) -> Candidate:
        db.session.add(candidate)
        db.session.commit()
        return candidate

    @staticmethod
    def fetch_candidate_by_token(token: str) -> Union[Candidate, None]:
        return db.session.query(Candidate).\
            filter_by(token=token).one_or_none()
