"""
Dependencies: json-rpc
    pip install json-rpc
"""
# Libraries
import json
import requests
import sys

# Relative imports
from credentials import AUTH

# Constants
URL = "http://127.0.0.1:8332"
PAYLOAD = {
        "method": "",
        "params": [],
        "id": 1,
}


# Functions
def makeRequest(payload, head={}):
    response = requests.post(URL, data=json.dumps(payload), headers=head,
                             auth=AUTH).json()
    return response['result']


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must provide at least the method.")
        exit(1)
    else:
        method = sys.argv[1]
        params = sys.argv[2:]

    p = PAYLOAD
    p['method'] = method
    p['params'] = params

    # Wrapper: decoderawtransaction from transaction id
    if method == "decoderawtransaction" and len(params[0]) == 64:
        aux = {
            "method": "getrawtransaction",
            "params": params,
            "id": 1,
        }
        tx = makeRequest(aux)
        p['params'] = [tx]

    # Request
    response = makeRequest(p)

    # Print response
    print()
    print(response)
