import flask
from infrastructure.view_modifiers import response
from services.query import get_data

blueprint = flask.Blueprint('index', __name__, template_folder='templates')


# ################### INDEX #################################

@blueprint.route('/home')
@response(template_file='index.html')
def index():

    data = get_data()
    data_dict = data.to_dict()

    return {'data': data_dict}
