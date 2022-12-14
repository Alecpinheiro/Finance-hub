from flask import Flask

app = Flask(__name__)
app.debug = True

from project.users.users_controller import *
from project.categories.cat_controller import *
from project.currencies.currencies_controller import *
from project.transaction_type.transaction_controller import *
from project.category_subtype.sub_cat_controller import *
