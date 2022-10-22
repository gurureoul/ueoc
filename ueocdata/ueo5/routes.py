from flask import Blueprint, render_template

ueo5 = Blueprint('ueo5', __name__, url_prefix='/ueo5')

@ueo5.route('/')
def index():
    return render_template('ueo5/index.html')