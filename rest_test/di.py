from flask import Flask
from flask_mail import Mail
from injector import Module, provider, singleton


class MailModule(Module):
    @provider
    @singleton
    def provide_ext(self, app: Flask) -> Mail:
        return Mail(app)
