from flask import Blueprint, render_template, request, redirect, url_for

from aws_lex import AWSLex
from forms import CreateBotForm

lexi = Blueprint('lexi', __name__, url_prefix='/cms/lexi')

@lexi.route('/', methods=["GET"])
def index():
    lex = AWSLex()      
    bots = lex.get_bots()
    return render_template('cms/lexi/index.html', bots=bots)

@lexi.route('/delete-bot', methods=["POST"])
def delete_bot():
    lex = AWSLex()
    if request.form.get('delete_bot'):
        lex.delete_bot(request.form['delete_bot'])
    return redirect(url_for('lexi.index'))

@lexi.route('/create-bot', methods=["GET", "POST"])
def create_bot():
    cb_form = CreateBotForm()
    if cb_form.validate_on_submit():
        lex = AWSLex()
        try:
            lex.create_bot(request.form['name'])
            return redirect(url_for('lexi.index'))
        except Exception as e:
            print(e)
            return redirect(request.referrer)
    return render_template('cms/lexi/create-bot.html', cb_form=cb_form)