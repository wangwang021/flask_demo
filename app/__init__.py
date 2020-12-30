from flask import Flask
from flask_cors import CORS

app=Flask(__name__)

from .views import *
from .user import user

app.register_blueprint(user)

CORS(app, resources={r"/*": {"origins": "*"}})