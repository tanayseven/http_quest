from click.testing import CliRunner

from http_quiz.app import create_new_admin, app
from http_quiz.user.model import User
from http_quiz.user.repo import UserRepo
from test.base import DatabaseTest


class TestCli(DatabaseTest):
    def test_user_should_be_created_from_command_line_function_create_new_admin_is_called(self):
        with app.app_context():
            email = 'someoneelse@somedomain.com'
            runner = CliRunner()
            result = runner.invoke(create_new_admin, [email])
            assert result.exit_code == 0
            saved_user = UserRepo.fetch_user_by_email(email)
            assert saved_user is not None

    def test_user_should_not_be_created_when_a_user_already_exists(self):
        with app.app_context():
            UserRepo.add(User(email='someone@somedomain.com', password='password'))
            email = 'someone@somedomain.com'
            runner = CliRunner()
            runner.invoke(create_new_admin, [email])
            result = runner.invoke(create_new_admin, [email])
            assert result.exit_code == -1
