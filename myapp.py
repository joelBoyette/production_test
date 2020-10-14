import flask

app = flask.Flask(__name__)
app.secret_key = 'some secret key'


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from views import test_views
    app.register_blueprint(test_views.blueprint)


if __name__ == '__main__':
    main()
