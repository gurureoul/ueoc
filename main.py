from ueocdata import create_app
import os
import uuid

# get the current directory of the main.py file
basedir = os.path.abspath(os.path.dirname(__file__))

# check to see if there is an instance folder, since it's not
# committed to source control
if not os.path.exists(basedir + '/instance'):
    os.makedirs(basedir + '/instance')

# create at an os.path to the config file for flask
cfg_file = os.path.join(basedir, 'instance/flask.cfg')

# only if it doesn't already exist, create it for the first time
if not os.path.exists(cfg_file):
    # and randomly generate a UUID for the secret key
    secret_key = uuid.uuid4()
    with open(cfg_file, 'w+') as tf:
        # add the secret key to the config file
        tf.write(f"SECRET_KEY='{secret_key}'")
        tf.write(f"SQLALCHEMY_DATABASE_URI='sqlite:///test.db'")
app = create_app()

if __name__ == '__main__':
    # 'app' gets imported by the wsgi, so having this in main
    # shouldn't run on the production server
    app.run(debug=True)