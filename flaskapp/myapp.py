import flask
import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
import flaskapp.data.db_session as db_session

app = flask.Flask(__name__)
app.secret_key = 'some secret key'


def main():
    config()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'production_test.sqlite').replace('\\', '/')

    db_session.global_init(db_file)


def register_blueprints():
    from flaskapp.views import test_views
    app.register_blueprint(test_views.blueprint)


def config():
    register_blueprints()
    setup_db()


if __name__ == '__main__':
    main()
else:
    config()


