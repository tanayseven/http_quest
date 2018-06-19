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
    def add_or_update_problem_input_output(input_: dict, output: dict, candidate: Candidate, problem_number: int):
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(candidate)
        if problem_input_output is None:
            db.session.add(SequentialQuiz(
                candidate_id=candidate.id,
                problem_number=problem_number,
                input=input_,
                output=output,
                attempts=1,
                status=str(QuestionStatus.PENDING),
            ))
        else:
            problem_input_output.input = input_
            problem_input_output.output = output
            problem_input_output.attempts += 1
            problem_input_output.status = str(QuestionStatus.PENDING),
            db.session.add(problem_input_output)
        db.session.commit()
