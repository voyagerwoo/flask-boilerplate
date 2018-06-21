from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/info', methods=['GET'])
def info():
    return '<h1>FLASK DOCKERIZE</h1>' \
           '<p>awskrug flask dockerize example</p>'


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return 'Not Found', 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', ('', error))
    return 'Internal Server Error', 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', ('', error))
    return 'Internal Server Error', 500
