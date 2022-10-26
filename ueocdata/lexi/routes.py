from flask import Blueprint, render_template

lexi = Blueprint('lexi', __name__, url_prefix='/cms/lexi')

@lexi.route('/')
def index():
    return render_template('cms/lexi/index.html')

