import flask
from werkzeug.wsgi import DispatcherMiddleware

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)

app.config.from_object('app_name.config')

app.config.from_envvar('app_name_SETTINGS', silent=True)

import app_name
import app_name.authorization
import app_name.sql
import app_name.views
import app_name.config
