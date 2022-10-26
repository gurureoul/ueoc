from flask import Blueprint, render_template, request, redirect, url_for

from aws_lex import AWSLex

lexi = Blueprint('lexi', __name__, url_prefix='/cms/lexi')

@lexi.route('/', methods=["GET", "POST"])
def index():
    lex = AWSLex()      
    bots = lex.get_bots()
    return render_template('cms/lexi/index.html', bots=bots)

@lexi.route('/delete-bot', methods=["POST"])
def delete_bot():
    lex = AWSLex()
    if request.form.get('delete_bot'):
        lex.delete_bot(request.form['delete_bot'])
    return redirect(request.referrer)