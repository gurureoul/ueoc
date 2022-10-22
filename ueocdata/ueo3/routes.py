from flask import Blueprint, render_template

ueo3 = Blueprint('ueo3', __name__, url_prefix='/ueo3')

@ueo3.route('/')
def index():
    return render_template('ueo3/index.html')