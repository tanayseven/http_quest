import os


def apply_dev_config(app):
    app.config.update(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        LOCALE=os.environ.get('APP_LOCALE'),
        JWT_AUTH_USERNAME_KEY='email',
        JWT_AUTH_PASSWORD_KEY='password',
        JWT_AUTH_URL_RULE='/user/login',
        MAIL_SERVER='mailcatcher',
        MAIL_PORT='1025',
        MAIL_SUPPRESS_SEND=False,
        MAIL_DEFAULT_SENDER='noreply@resttest.com',
    )
