from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    from .public import public

    app.register_blueprint(public, url_prefix='/')

    return app
    