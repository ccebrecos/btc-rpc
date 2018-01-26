from flask import Flask
from flask import request
import pyrpc

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/<method>")
def method(method):
    searchword = request.args.get('arg', '')
    payload = {
            "method": method,
            "params": [searchword],
            "id": 1,
    }
    result = pyrpc.makeRequest(payload)

    return result
