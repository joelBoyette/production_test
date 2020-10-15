import flask

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
