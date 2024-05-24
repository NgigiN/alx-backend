from flask import Flask
from flask import request
from flask_babel import Babel


def get_locale():
    pass


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)

from app import routes
