from flask.blueprints import Blueprint

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return 'Index'


@bp.route('/hello')
def hello():
    return "Hello, Flask"