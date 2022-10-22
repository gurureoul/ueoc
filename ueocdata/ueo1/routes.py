from flask import Blueprint, render_template

ueo1 = Blueprint('ueo1', __name__, url_prefix='/ueo1')

@ueo1.route('/')
def index():
    return render_template('ueo1/index.html')