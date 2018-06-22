from typing import Union, Tuple

from sqlalchemy import desc, join

from http_quiz.ext import db
from http_quiz.quiz.model import Candidate, SequentialQuiz, QuestionStatus


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
    def fetch_latest_answer_by_candidate(candidate: Candidate) -> Union[None, SequentialQuiz]:
        result = db.session.query(Candidate, SequentialQuiz).select_from(
            join(Candidate, SequentialQuiz, SequentialQuiz.candidate_id == Candidate.id)) \
            .filter(Candidate.id == candidate.id).order_by(
            desc(SequentialQuiz.problem_number)
        ).limit(1).one_or_none()
        return None if result is None else result[1]

    @staticmethod
    def add_or_update_problem_input_output(input_: list, output: dict, candidate: Candidate, problem_number: int):
        quiz_repo = QuizRepo.fetch_latest_answer_by_candidate(candidate)
        if quiz_repo is None:
            db.session.add(SequentialQuiz(
                candidate_id=candidate.id,
                problem_number=problem_number,
                input=input_,
                output=output,
                attempts=1,
                status=str(QuestionStatus.PENDING),
            ))
        else:
            quiz_repo.input = input_
            quiz_repo.output = output
            quiz_repo.attempts += 1
            quiz_repo.status = str(QuestionStatus.PENDING),
            db.session.add(quiz_repo)
        db.session.commit()

    @staticmethod
    def set_status_to(status: QuestionStatus, question_attempt: SequentialQuiz):
        question_attempt.status = str(status)
        db.session.add(question_attempt)
        db.session.commit()
