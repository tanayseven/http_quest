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
    def fetch_latest_answer_by_candidate(candidate: Candidate) -> Tuple[Candidate, SequentialQuiz]:
        sql = db.session.query(Candidate, SequentialQuiz).select_from(join(Candidate, SequentialQuiz, SequentialQuiz.candidate_id == Candidate.id))\
            .filter(Candidate.id == candidate.id).order_by(
                desc(SequentialQuiz.problem_number)
            ).limit(1)
        return sql.one_or_none()

    @staticmethod
    def add_or_update_problem_input_output(input_: list, output: dict, candidate: Candidate, problem_number: int):
        result = QuizRepo.fetch_latest_answer_by_candidate(candidate)
        if result is None:
            db.session.add(SequentialQuiz(
                candidate_id=candidate.id,
                problem_number=problem_number,
                input=input_,
                output=output,
                attempts=1,
                status=str(QuestionStatus.PENDING),
            ))
        else:
            candidate, sequential_quiz = result
            sequential_quiz.input = input_
            sequential_quiz.output = output
            sequential_quiz.attempts += 1
            sequential_quiz.status = str(QuestionStatus.PENDING),
            db.session.add(sequential_quiz)
        db.session.commit()

    @staticmethod
    def set_status_to(status: QuestionStatus, question_attempt: SequentialQuiz):
        question_attempt.status = str(status)
        db.session.add(question_attempt)
        db.session.commit()
