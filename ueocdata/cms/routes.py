from flask import Blueprint, render_template

cms = Blueprint('cms', __name__, url_prefix='/cms')

@cms.route('/')
def index():
    return render_template('cms/index.html')

@cms.route('/lexi')
def lexi():
    return render_template('cms/lexi.html')