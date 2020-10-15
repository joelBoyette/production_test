import flask
import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)
app.secret_key = 'some secret key'


def main():
    config()
    app.run(debug=True)


def register_blueprints():
    from flaskapp.views import test_views
    app.register_blueprint(test_views.blueprint)


def config():
    register_blueprints()


if __name__ == '__main__':
    main()
else:
    config()


