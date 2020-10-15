import flask
from flaskapp.infrastructure.view_modifiers import response
# from flaskapp.services.query import get_data

blueprint = flask.Blueprint('index', __name__, template_folder='templates')


# ################### INDEX #################################

@blueprint.route('/')
@response(template_file='index.html')
def index():

    # data = get_data()
    # data_dict = data.to_dict()
    #
    # return {'data': data_dict}

    return {}
