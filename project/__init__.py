from flask import Flask

app = Flask(__name__)
app.debug = True

from project.users.controller import *
from project.categories.cat_controller import *
