from flask import Flask

from .public.routes import public
from .ueo1.routes import ueo1
from .ueo3.routes import ueo3
from .ueo4.routes import ueo4
from .ueo5.routes import ueo5
from .cms.routes import cms
from .lexi.routes import lexi

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('flask.cfg')

    app.register_blueprint(public)
    app.register_blueprint(ueo1)
    app.register_blueprint(ueo3)
    app.register_blueprint(ueo4)
    app.register_blueprint(ueo5)
    app.register_blueprint(cms)
    app.register_blueprint(lexi)
    return app
