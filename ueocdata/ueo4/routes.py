from flask import Blueprint, render_template

ueo4 = Blueprint('ueo4', __name__, url_prefix='/ueo4')

@ueo4.route('/')
def index():
    return render_template('ueo4/index.html')