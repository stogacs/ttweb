from flask import Flask
from flask import jsonify
from flask import make_response

app = Flask(__name__)


database = {'names': []}  # type: ignore


def run():
    app.run(debug=True)  # nosec


@app.route('/')
def index():
    return 'Tiny Tiny Web API'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'


@app.route('/json/<name>')
def json_route(name):
    data = '{"name": "%s"}' % name
    r = make_response(data)
    r.mimetype = 'application/json'
    return r


@app.route('/jsonify/<string>')
def jsonify_route(string):
    data = {"string": string}
    return jsonify(data)


@app.route('/create/<name>', methods=['POST'])
def post_name(name):
    database['names'].append(name)
    return jsonify({'message': 'success'})


@app.route('/names')
def get_names():
    return jsonify(database['names'])


@app.errorhandler(404)
def not_found_handler(e):
    return 'Page not found!'
