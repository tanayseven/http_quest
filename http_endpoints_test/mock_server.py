from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=('GET',))
def something():
    data = {'something': 'the data'}
    return jsonify(data)


@app.route('/send', methods=('POST',))
def something_else():
    data = {'something': 'something extra'}
    return jsonify(data)
