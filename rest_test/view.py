from flask import Blueprint, jsonify
from flask_mail import Message

from rest_test.extensions import mail

root_view = Blueprint('root', __name__)


@root_view.route('/', methods=('GET',))
def root_get():
    data = {'message': 'this is the / please go to /login for any further activity'}
    return jsonify(data)


@root_view.route('/login', methods=('GET',))
def login_get():
    data = {
        'message': 'to login, please POST `login_format` on /login',
        'login_format': {'email': '<your_email>', 'password': '<your_password>'}
    }
    return jsonify(data)


@root_view.route('/forgot_password', methods=('POST',))
def password_reset():
    data = {
        'message': 'you should have received an email with password reset instructions',
    }
    msg = Message('Password Reset Instructions', recipients=['someone@mail.com'], body='this is the body of the message')
    mail.send(msg)
    return jsonify(data)
