# encoding: utf8

import os

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask.ext.login import LoginManager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from flask.ext.openid import OpenID
from config import basedir
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from flask.ext.mail import Mail
mail = Mail(app)

from momentjs import Momentjs
app.jinja_env.globals['momentjs'] = Momentjs

from flask.ext.babel import Babel
babel = Babel(app)

from app import views, models
