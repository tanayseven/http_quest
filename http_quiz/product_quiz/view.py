from flask import Blueprint, jsonify, g, request
from injector import inject

from http_quiz.product_quiz.problem_statements import ProductCollection, Product
from http_quiz.product_quiz.translations import _
from http_quiz.quiz.model import QuestionStatus
from http_quiz.quiz.quiz import candidate_token_required
from http_quiz.quiz.repo import QuizRepo
from http_quiz.utilities import RandomWrapper

products_view = Blueprint('product_quiz', __name__)


@products_view.route('/product_quiz/')
def root():
    data = {'message': 'You are at the root of all the endpoints. Please go to /product_quiz/problem_statement/ '
                       'for the first problem'}
    return jsonify(data), 200


welcome_message = _('Welcome to the  product quiz.')
this_stage_number_is = _('This problem number is {0}.')
problem_statement = [
    _('Compute the count for the total number of products in the list given via input'),
    _('Awesome, you\'ve solved the first problem. Active products are those for which '
      'current date time fall within start and end date of the current date. Compute the count of all such products')
]
the_input_output_url_is = _(
    'The input url for getting the test data is GET on /product/{0}/input/ and the data will '
    'be in JSON. And you will have to respond with the output on the URL by doing a POST on /product_quiz/{0}/output/.'
)
example_included_here = _('The examples for the sample input and output are included here.')

solved_successfully = _('You\'ve solved this problem successfully.')
wrong_solution = _('Wrong solution. Please attempt again with a new input.')
already_attempted = _('You\'ve already attempted this problem, please fetch a new input from the input URL.')

first_problem = {
    'message': ' '.join((
        welcome_message,
        this_stage_number_is.format(1),
        problem_statement[0],
        the_input_output_url_is.format(1),
        example_included_here,
    )),
    'example': {
        'input': {
            'end_date': '',
        },
        'output': {
            'end_date': '',
        }
    }
}

second_problem = {
    'message': ' '.join((
        this_stage_number_is.format(2),
        problem_statement[1],
        the_input_output_url_is.format(2),
        example_included_here,
    )),
    'example': {
        'input': {
            'end_date': '',
        },
        'output': {
            'end_date': '',
        }
    }
}


@products_view.route('/product_quiz/problem_statement', methods=('GET',))
@candidate_token_required('sequential', 'product')
def problem_statement():
    latest_problem_attempt = QuizRepo.fetch_latest_answer_by_candidate(g.candidate)
    if latest_problem_attempt is None or latest_problem_attempt.pending_or_wrong(problem_no=1):
        return jsonify({'message': first_problem['message']}), 200
    elif latest_problem_attempt.has_been_solved(problem_no=1):
        return jsonify({'message': second_problem['message']}), 200
    data = {'message': 'Something went wrong'}
    return jsonify(data), 500


@products_view.route('/product_quiz/<int:problem_number>/input', methods=('GET',))
@candidate_token_required('sequential', 'product')
@inject
def problem_input(problem_number, random: RandomWrapper = RandomWrapper()):
    input_ = ProductCollection.generate_products(random.randrange(1, 20))
    input_dict = ProductCollection.to_dict(input_)
    latest_answer_by_candidate = QuizRepo.fetch_latest_answer_by_candidate(g.candidate)
    if latest_answer_by_candidate is None:
        output = Product.solution_count(input_)
        QuizRepo.add_or_update_problem_input_output(input_dict, output, g.candidate, problem_number)
    elif latest_answer_by_candidate.has_been_solved(problem_no=problem_number-1):
        output = Product.solution_active_count(input_)
        QuizRepo.add_or_update_problem_input_output(input_dict, output, g.candidate, problem_number)
    return jsonify(input_dict), 200


@products_view.route('/product_quiz/<int:problem_number>/output', methods=('POST',))
@candidate_token_required('sequential', 'product')
def problem_output(problem_number):
    latest_problem_attempt = QuizRepo.fetch_latest_answer_by_candidate(g.candidate)
    if latest_problem_attempt is None:
        return jsonify({'message': 'Could not find your previous attempt to fetch input'}), 404
    elif latest_problem_attempt.status == str(QuestionStatus.WRONG):
        return jsonify({'message': already_attempted}), 400
    elif latest_problem_attempt.problem_number == problem_number \
            and latest_problem_attempt.status == str(QuestionStatus.PENDING)\
            and latest_problem_attempt.output == request.get_json():
        QuizRepo.set_status_to(QuestionStatus.CORRECT, latest_problem_attempt)
        return jsonify({'message': solved_successfully}), 200
    QuizRepo.set_status_to(QuestionStatus.WRONG, latest_problem_attempt)
    return jsonify({'message': wrong_solution}), 400
