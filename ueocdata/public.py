from flask import Blueprint, render_template

public = Blueprint('public', __name__)

@public.route('/')
def main():
    return render_template('main.html')