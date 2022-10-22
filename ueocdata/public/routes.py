from flask import Blueprint, render_template

public = Blueprint('public', __name__, url_prefix='/')

@public.route('/')
def index():
    return render_template('main.html')
