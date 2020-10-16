import flask
from flaskapp.infrastructure.view_modifiers import response
from flaskapp.services.query import find_person

blueprint = flask.Blueprint('index', __name__, template_folder='templates')


# ################### INDEX #################################

@blueprint.route('/')
@response(template_file='index.html')
def index():

    person = find_person('Joel')

    if person:
        print(person.first_name)
        return {'data': person.first_name}

    return {'data': ''}
