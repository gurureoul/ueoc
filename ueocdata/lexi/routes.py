from flask import Blueprint, render_template

from aws_lex import AWSLex

lexi = Blueprint('lexi', __name__, url_prefix='/cms/lexi')

@lexi.route('/')
def index():
    lex = AWSLex()
    bots = lex.get_bots()
    return render_template('cms/lexi/index.html', bots=bots)

