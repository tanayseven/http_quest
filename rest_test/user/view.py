from flask import jsonify, Blueprint
from flask_mail import Message

from rest_test.extensions import mail

user_view = Blueprint('user', __name__)


@user_view.route('/user/login', methods=('GET',))
def login_get():
    data = {
        'message': 'to login, please POST `login_format` on /login',
        'login_format': {'email': '<your_email>', 'password': '<your_password>'}
    }
    return jsonify(data)


@user_view.route('/user/forgot_password', methods=('POST',))
def password_reset():
    data = {
        'message': 'you should have received an email with password reset instructions',
    }
    msg = Message('Password Reset Instructions', recipients=['someone@mail.com'],
                  body='this is the body of the message')
    mail.send(msg)
    return jsonify(data)
